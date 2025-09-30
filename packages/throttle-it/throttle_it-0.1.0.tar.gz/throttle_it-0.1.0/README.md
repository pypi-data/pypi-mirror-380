![Python Version from PEP 621 TOML](https://img.shields.io/python/required-version-toml?tomlFilePath=https%3A%2F%2Fraw.githubusercontent.com%2Fsondalex%2Fthrottle-it%2Fmaster%2Fpyproject.toml)

# throttle-it <a href="https://sondalex.github.io/throttle-it"><img src="assets/drawing.png" align="right" height="138" alt="throttle-it website" /></a>

Throttle your API calls

## Installation

```bash
pip install throttle-it
```

## Usage

```python
from throttle_it import throttle, Duration
from requests import Session

@throttle(
    Duration.MINUTE,
    limit_header_name="X-RateLimit-Limit",
    remaining_header_name="X-RateLimit-Remaining",
    reset_header_name="X-RateLimit-Reset",
)
def get(session: Session, ...):
    return session.get(...)
```

## Development

**Install dev dependencies**

```bash
pip install ".[dev]"
```

**Run pre-commits**

```bash
uv tool run pre-commit install
```
