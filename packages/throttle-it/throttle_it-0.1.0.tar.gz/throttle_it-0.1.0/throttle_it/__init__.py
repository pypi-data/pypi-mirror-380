import logging
import random
import sys
import time
from dataclasses import dataclass
from typing import Callable, List, Optional, Protocol, Sequence, Union

from pyrate_limiter import Duration
from pyrate_limiter import Limiter as PyLimiter
from pyrate_limiter import Rate
from requests import Response, Session

logger = logging.getLogger(__name__)


class RequestFuncType(Protocol):
    def __call__(self, session: Session, *args, **kwargs) -> Response:
        pass


ParseCounts = Callable[[str], List[int]]
ParseResets = Callable[[str], List[int]]
IdentityFn = Callable[..., str]
Number = Union[int, float]


def _format_duration(seconds: int) -> str:
    """Format seconds into a human-readable string like '2h 3m 10s'."""
    if seconds < 60:
        return f"{seconds}s"
    minutes, sec = divmod(seconds, 60)
    if minutes < 60:
        return f"{minutes}m {sec}s"
    hours, minutes = divmod(minutes, 60)
    if hours < 24:
        return f"{hours}h {minutes}m {sec}s"
    days, hours = divmod(hours, 24)
    return f"{days}d {hours}h {minutes}m {sec}s"


def _wait_with_bar(total: int) -> None:
    if total <= 0:
        return

    spinner = "⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏"
    steps = len(spinner)

    if sys.stdout.isatty():
        for remaining in range(total, 0, -1):
            human = _format_duration(remaining)
            for i in range(steps):
                sys.stdout.write(
                    f"\r{spinner[i]} Waiting {human} until rate-limit reset..."
                )
                sys.stdout.flush()
                time.sleep(1 / steps)
        sys.stdout.write("\r✅ Resuming requests...                    \n")
        sys.stdout.flush()
    else:
        logger.info("Sleeping %s until rate-limit reset", _format_duration(total))
        time.sleep(total)


def _split_ints(s: str) -> List[int]:
    """Parse delimited integers from a header (supports '/' or ',')."""
    if s is None:
        raise ValueError("Input string cannot be None.")
    sep = "/" if "/" in s else ("," if "," in s else None)
    if sep is None:
        return [int(s.strip())]
    return [int(x.strip()) for x in s.split(sep) if x.strip()]


def _best_effort_parse_resets(
    reset_raw: Optional[str], parse_resets: Optional[ParseResets]
) -> Optional[List[int]]:
    """Parse reset header using a custom parser or a best-effort fallback."""
    if not reset_raw:
        return None
    if parse_resets:
        try:
            return parse_resets(reset_raw)
        except Exception:
            return None
    try:
        return _split_ints(reset_raw)
    except Exception:
        try:
            return [int(reset_raw)]
        except Exception:
            return None


def _validate_policy_vs_windows(
    policy_counts: Sequence[int], windows: Sequence[Duration]
) -> bool:
    """Ensure policy shape matches configured windows."""
    return len(policy_counts) == len(windows)


def _build_rates(
    policy_counts: Sequence[int], windows: Sequence[Duration]
) -> List[Rate]:
    """Make pyrate-limiter Rate objects for all windows."""
    return [Rate(q, w) for q, w in zip(policy_counts, windows)]


def _compute_sleep_until(
    remaining: Sequence[int], resets: Optional[Sequence[int]]
) -> int:
    """
    Compute maximum sleep (seconds) among exhausted windows using provided resets.

    Returns
    -------
    int
        Seconds to sleep (0 if no sleep is needed or resets are not usable).
    """
    if not resets or not remaining:
        return 0
    now = int(time.time())
    waits: List[int] = []
    # If resets length mismatches, treat as single timestamp
    if len(resets) != len(remaining):
        return max(0, resets[0] - now)
    for r, ts in zip(remaining, resets):
        if r <= 0:
            waits.append(max(0, ts - now))
    return max(waits) if waits else 0


@dataclass
class _HeaderNames:
    limit: str
    remaining: str
    reset: Optional[str] = None


class _ServerSyncedLimiter:
    """
    Thin wrapper around pyrate-limiter for clarity.

    Responsibilities:
    - Pre-call token acquisition (blocking pacing).
    - Post-call reconciliation with headers (policy rebuild + optional reset sleep).
    """

    def __init__(
        self,
        windows: Sequence[Duration],
        max_block: Union[int, Duration],
        parse_counts: ParseCounts,
        parse_resets: Optional[ParseResets],
        headers: _HeaderNames,
        identity: Union[str, IdentityFn] = "global",
    ):
        self.windows = list(windows)
        self.max_block = max_block
        self.parse_counts = parse_counts
        self.parse_resets = parse_resets
        self.headers = headers
        self.identity = identity

        # Track server state
        self._last_remaining: Optional[list[int]] = None
        self._last_resets: Optional[list[int]] = None

        # Start safe: 1 request per second until we learn policy
        self._limiter = PyLimiter(
            [Rate(1, Duration.SECOND)], raise_when_fail=False, max_delay=max_block
        )

    def _resolve_identity(self, *args, **kwargs) -> str:
        return (
            self.identity(*args, **kwargs) if callable(self.identity) else self.identity
        )

    def acquire(self, *args, **kwargs) -> None:
        """
        Block until a token is available (pyrate-limiter pacing).
        """
        lid = self._resolve_identity(*args, **kwargs)
        if self._limiter.try_acquire(lid) is False:
            # Rare: internal pacing exceeded max_delay, back off a little
            time.sleep(0.25)
            self._limiter.try_acquire(lid)

    def reconcile(self, response: Response) -> None:
        """
        Update limiter from headers and track remaining/reset info.
        """
        h = response.headers

        remaining_counts = None
        remaining_raw = h.get(self.headers.remaining)
        if remaining_raw:
            try:
                remaining_counts = self.parse_counts(remaining_raw)
            except Exception:
                remaining_counts = None

        resets = None
        if self.headers.reset:
            resets = _best_effort_parse_resets(
                h.get(self.headers.reset), self.parse_resets
            )

        self._last_remaining = remaining_counts
        self._last_resets = resets

        policy_raw = h.get(self.headers.limit)
        if not policy_raw:
            return  # NOTE: keep existing limiter

        try:
            policy_counts = self.parse_counts(policy_raw)
        except Exception:
            return

        if _validate_policy_vs_windows(policy_counts, self.windows):
            self._limiter = PyLimiter(
                _build_rates(policy_counts, self.windows),
                raise_when_fail=False,
                max_delay=self.max_block,
            )
        # If counts/windows mismatch, we skip rebuild but keep stored state


def throttle(
    *windows: Duration,
    limit_header_name: str,
    remaining_header_name: str,
    reset_header_name: Optional[str] = None,
    identity: Union[str, IdentityFn] = "global",
    parse_counts: ParseCounts = _split_ints,
    parse_resets: Optional[ParseResets] = None,
    max_block: Union[int, Duration] = Duration.MINUTE,
):
    """
    Multi-window, server-synchronized rate limiter decorator.

    This decorator uses `pyrate-limiter` to enforce API rate limits defined in
    response headers. It supports an arbitrary number of windows (e.g., per
    minute, per hour), automatically rebuilds the limiter from policy headers,
    and can synchronize with the server's reset timestamp.

    Parameters
    ----------
    *windows : Duration
        One ``Duration`` object per rate-limit window.
        For example, ``Duration.MINUTE, Duration.HOUR`` corresponds to a
        two-window policy like "500 requests per minute" and
        "5000 requests per hour".
    limit_header_name : str
        Name of the HTTP header that provides the maximum allowed requests.
        The value must contain one or more integers matching the number of
        windows, e.g. ``"10/500"`` for two windows.
    remaining_header_name : str
        Name of the HTTP header that provides the remaining quota.
        The format must match ``limit_header_name``.
    reset_header_name : str, optional
        Name of the HTTP header that provides the reset timestamp(s), by default None.
        If present, the value may be a single UNIX timestamp or multiple
        timestamps (one per window, same order as `*windows`).
        If any window reaches zero remaining requests, the decorator will
        sleep until the corresponding reset.
    identity : str or callable, default="global"
        Unique identifier for the limiter. If a callable, it must accept the
        decorated function's arguments and return a string (e.g., per-API-key).
        This ensures separate rate limiting per identity.
    parse_counts : callable, default=_split_ints
        Function to parse header values (limit/remaining) into a list of
        integers. Default parser supports values like ``"10/500"`` or
        ``"10,500"``.
    parse_resets : callable, optional
        Function to parse the reset header value into a list of UNIX timestamps.
        If None, the same parser as `parse_counts` is used as a fallback.
    max_block : int or Duration, default=Duration.MINUTE
        Maximum time the internal `Limiter` may block automatically when
        enforcing rate limits. If exceeded, a short sleep/retry loop is used.

    Returns
    -------
    decorator: callable
        A function decorator that applies rate limiting to the wrapped function.

    Notes
    -----
    - The decorated function must return a ``requests.Response`` object.
    - The limiter is updated dynamically from server headers after each
      response.
    - If headers are missing or malformed, the existing limiter configuration
      is retained.

    Examples
    --------
    Single-window usage (per-minute policy):

    >>> import requests
    >>> from throttle_it import Duration, throttle
    >>>
    >>>
    >>> @throttle(
            Duration.MINUTE,
            limit_header_name="X-RateLimit-Limit",
            remaining_header_name="X-RateLimit-Remaining",
            reset_header_name="X-RateLimit-Reset",
        )
        def get(session, url):
            return session.get(url)
    >>>
    >>>
    >>> with requests.Session() as s:
            r = get(s, "https://httpbin.org/get")

    Multi-window usage (per-minute and per-hour policy):

    >>> @throttle(
            Duration.MINUTE, Duration.HOUR,
            limit_header_name="X-RateLimit-Limit",
            remaining_header_name="X-RateLimit-Remaining",
            reset_header_name="X-RateLimit-Reset",
        )
    >>> def fetch(session, url):
            return session.get(url)
    """
    if not windows:
        raise ValueError(
            "Provide at least one Duration window (e.g., Duration.MINUTE)."
        )

    hdr = _HeaderNames(
        limit=limit_header_name,
        remaining=remaining_header_name,
        reset=reset_header_name,
    )
    controller = _ServerSyncedLimiter(
        windows=windows,
        max_block=max_block,
        parse_counts=parse_counts,
        parse_resets=parse_resets,
        headers=hdr,
        identity=identity,
    )

    def decorator(func: RequestFuncType):
        def wrap(*args, **kwargs):
            base_delay = 1
            retry_count = 0
            # NOTE: If there's an exhaustion of remote server, the server is likely to
            # close the connection
            while True:
                controller.acquire(*args, **kwargs)
                response = func(*args, **kwargs)
                controller.reconcile(response)

                # Handle 429 with retry-after logic
                if response.status_code == 429:
                    # 1) Try per-window reset (best: only for exhausted windows)
                    sleep_for = _compute_sleep_until(
                        controller._last_remaining or [],
                        controller._last_resets or [],
                    )
                    # 2) Fallback to Retry-After
                    if not sleep_for:
                        ra = response.headers.get("Retry-After")
                        if ra and ra.isdigit():
                            sleep_for = int(ra)
                    # 3) Last-resort backoff
                    if not sleep_for:
                        sleep_for = base_delay * (2**retry_count) + random.uniform(0, 1)

                    _wait_with_bar(int(sleep_for))
                    retry_count += 1
                    continue

                return response

        return wrap

    return decorator


__all__ = ["throttle", "Duration"]
