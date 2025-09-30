import time
from unittest.mock import patch

import pytest
import requests
from pyrate_limiter import Rate

import throttle_it
from throttle_it import Duration


def test_split_ints_variants():
    assert throttle_it._split_ints("10/20") == [10, 20]
    assert throttle_it._split_ints("10,20") == [10, 20]
    assert throttle_it._split_ints("15") == [15]
    with pytest.raises(ValueError):
        throttle_it._split_ints(None)


def test_best_effort_parse_resets_with_custom_parser():
    def parser(s):
        return [int(x) + 1 for x in s.split("/")]

    assert throttle_it._best_effort_parse_resets("10/20", parser) == [11, 21]


def test_best_effort_parse_resets_with_default_and_fallback():
    assert throttle_it._best_effort_parse_resets("10/20", None) == [10, 20]
    now = str(int(time.time()) + 5)
    assert throttle_it._best_effort_parse_resets(now, None) == [int(now)]
    assert throttle_it._best_effort_parse_resets("notanumber", None) is None


def test_validate_policy_vs_windows_and_build_rates():
    counts = [10, 20]
    windows = [Duration.SECOND, Duration.MINUTE]
    assert throttle_it._validate_policy_vs_windows(counts, windows)
    rates = throttle_it._build_rates(counts, windows)
    assert all(isinstance(r, Rate) for r in rates)


def test_compute_sleep_until_single_and_multi():
    now = int(time.time())
    resets = [now + 2, now + 5]
    remaining = [0, 10]
    assert 0 <= throttle_it._compute_sleep_until(remaining, resets) <= 5

    assert throttle_it._compute_sleep_until([0, 0], [now + 1]) in (0, 1)


def make_response(headers: dict, status: int = 200):
    resp = requests.Response()
    resp.status_code = status
    resp._content = b"ok"
    resp.headers.update(headers)
    return resp


def test_acquire_and_reconcile_basic(monkeypatch):
    hdr = throttle_it._HeaderNames("Limit", "Remaining", "Reset")
    limiter = throttle_it._ServerSyncedLimiter(
        windows=[Duration.SECOND],
        max_block=Duration.SECOND,
        parse_counts=throttle_it._split_ints,
        parse_resets=None,
        headers=hdr,
        identity="id1",
    )

    # NOTE: Acquire should not raise
    limiter.acquire()

    # NOTE: With missing headers, reconcile does nothing
    resp = make_response({})
    limiter.reconcile(resp)  # NOTE: should not crash


def test_throttle_it_decorator(monkeypatch):
    now = int(time.time())

    @throttle_it.throttle(
        Duration.SECOND,
        limit_header_name="Limit",
        remaining_header_name="Remaining",
        reset_header_name="Reset",
    )
    def fake_get(session, url):
        return make_response(
            {
                "Limit": "5",
                "Remaining": "1",
                "Reset": str(now + 1),
            }
        )

    resp = fake_get(requests.Session(), "http://example.com")
    assert isinstance(resp, requests.Response)
    assert resp.status_code == 200


def test_throttle_it_requires_windows():
    with pytest.raises(ValueError):

        @throttle_it.throttle(
            limit_header_name="L",
            remaining_header_name="R",
        )
        def f():
            pass


def test_reconcile_updates_state():
    hdr = throttle_it._HeaderNames("Limit", "Remaining", "Reset")
    limiter = throttle_it._ServerSyncedLimiter(
        windows=[Duration.SECOND],
        max_block=1,
        parse_counts=throttle_it._split_ints,
        parse_resets=None,
        headers=hdr,
    )

    now = int(time.time())
    resp = make_response(
        {
            "Limit": "5",
            "Remaining": "0",
            "Reset": str(now + 3),
        }
    )

    limiter.reconcile(resp)

    # State updated, but no sleep here
    assert limiter._last_remaining == [0]
    assert abs(limiter._last_resets[0] - (now + 3)) <= 1


def test_throttle_it_retries_on_429(monkeypatch):
    """
    Verify that the decorator retries when a 429 is returned and respects Retry-After or Reset headers.
    """

    now = int(time.time())

    # Simulate: first call -> 429, second call -> success
    responses = [
        make_response(
            {
                "Limit": "5",
                "Remaining": "0",
                "Reset": str(now + 3),
                "Retry-After": "2",
            },
            status=429,
        ),
        make_response(
            {
                "Limit": "5",
                "Remaining": "4",
                "Reset": str(now + 3),
            },
            status=200,
        ),
    ]

    call_log = []

    @throttle_it.throttle(
        Duration.SECOND,
        limit_header_name="Limit",
        remaining_header_name="Remaining",
        reset_header_name="Reset",
    )
    def fake_get(session, url):
        call_log.append(url)
        return responses.pop(0)

    with (
        patch.object(time, "sleep") as mock_sleep,
        requests.Session() as s,
    ):
        resp = fake_get(s, "http://example.com")

    # We should have retried after the 429
    assert resp.status_code == 200
    assert call_log == ["http://example.com", "http://example.com"]

    # Sleep was called once with Retry-After = 2
    mock_sleep.assert_called_once()
    waited = mock_sleep.call_args[0][0]
    assert 0 <= waited <= 3


def test_throttle_it_retries_on_429_with_reset(monkeypatch):
    """
    Verify that when Retry-After is missing, the decorator uses x-ratelimit-reset
    to decide how long to sleep before retrying.
    """
    now = int(time.time())

    # Simulate: first call -> 429 with reset in 3s, second call -> success
    responses = [
        make_response(
            {
                "Limit": "5",
                "Remaining": "0",
                "Reset": str(now + 3),
                # No Retry-After header!
            },
            status=429,
        ),
        make_response(
            {
                "Limit": "5",
                "Remaining": "4",
                "Reset": str(now + 3),
            },
            status=200,
        ),
    ]

    call_log = []

    @throttle_it.throttle(
        Duration.SECOND,
        limit_header_name="Limit",
        remaining_header_name="Remaining",
        reset_header_name="Reset",
    )
    def fake_get(session, url):
        call_log.append(url)
        return responses.pop(0)

    with (
        patch.object(time, "sleep") as mock_sleep,
        requests.Session() as s,
    ):
        resp = fake_get(s, "http://example.com")

    # We should have retried after the 429
    assert resp.status_code == 200
    assert call_log == ["http://example.com", "http://example.com"]

    # Sleep was called once with ~3s
    mock_sleep.assert_called_once()
    waited = mock_sleep.call_args[0][0]
    assert 0 <= waited <= 3
