# Zipcodestack Python Client

Official Python wrapper for the Zipcodestack API.

- Docs: https://zipcodestack.com/docs/
- Built on: https://github.com/everapihq/everapi-python
- Example reference: https://github.com/everapihq/freecurrencyapi-python

## Installation

```bash
pip install zipcodestack
```

Install from source:

```bash
pip install git+https://github.com/everapihq/zipcodestack-python.git
```

## Quickstart

```python
import os
from zipcodestack import Client

client = Client(os.environ["ZIPCODESTACK_API_KEY"])  # or Client("YOUR_API_KEY")

# Retrieve API status & quota
print(client.status())

# Search postal/zip codes
print(client.search(codes=["1010", "1020"], country="AT"))

# Calculate distance between postal/zip codes
print(client.distance(code="99501", compare=["90210", "10001"], country="US", unit="km"))
```

## API

- `Client(api_key: str, *, base_url: str = "https://api.zipcodestack.com/v1", timeout: float | None = None)`
- `status()` → dict
- `search(*, codes: str | Iterable[str], country: str | None = None, **params)` → dict
- `distance(*, code: str, compare: str | Iterable[str], country: str | None = None, unit: str | None = None, **params)` → dict

See the official docs for accepted parameters and response formats: https://zipcodestack.com/docs/

## License

MIT

