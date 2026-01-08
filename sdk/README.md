# VAP Python SDK

Official Python client for VAP API.

## Installation

```bash
pip install vape-client
```

## Quick Start

```python
from vape_client import VAPClient

client = VAPClient(api_key="your_api_key")

# Generate an image
result = client.generate(prompt="A sunset over mountains")
print(result.image_url)

# Check balance
balance = client.get_balance()
print(f"Balance: ${balance.balance}")
```

## Context Manager

```python
with VAPClient(api_key="your_api_key") as client:
    result = client.generate(prompt="A futuristic city")
```

## Error Handling

```python
from vape_client import (
    VAPClient,
    VAPAuthenticationError,
    VAPInsufficientBalanceError,
    VAPRateLimitError,
)

try:
    result = client.generate(prompt="...")
except VAPAuthenticationError:
    print("Invalid API key")
except VAPInsufficientBalanceError:
    print("Add funds to continue")
except VAPRateLimitError:
    print("Too many requests")
```

## License

MIT
