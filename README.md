# VAP - Visual Asset Production Engine

AI-powered image and video generation for autonomous agents.

![Version](https://img.shields.io/badge/version-1.6.0-blue.svg)
![Python](https://img.shields.io/badge/python-3.11+-green.svg)
![License](https://img.shields.io/badge/license-MIT-yellow.svg)

## Features

- **Image Generation** - High-quality AI image generation
- **Video Generation** - AI-powered video creation
- **Multi-Protocol Support** - REST API, A2A Protocol, MCP Server
- **Production Ready** - Enterprise-grade reliability

## Quick Start

### Installation

```bash
pip install vape-client
```

### Basic Usage

```python
from vape_client import VAPClient

client = VAPClient(api_key="your_api_key")

# Generate an image
result = client.generate_image(
    prompt="A serene mountain landscape at sunset"
)

print(f"Image URL: {result.url}")
```

### Async Usage

```python
import asyncio
from vape_client import AsyncVAPClient

async def main():
    client = AsyncVAPClient(api_key="your_api_key")
    result = await client.generate_image(prompt="A futuristic cityscape")
    print(f"Image URL: {result.url}")

asyncio.run(main())
```

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/v3/generate` | POST | Create generation task |
| `/v3/tasks/{id}` | GET | Get task status |
| `/v3/tasks/{id}/result` | GET | Get task result |

## MCP Server

VAP supports the Model Context Protocol for Claude Desktop integration.

```json
{
  "mcpServers": {
    "vap": {
      "url": "https://api.vapagent.com/mcp"
    }
  }
}
```

## Documentation

- [API Reference](api/openapi.yaml)
- [SDK Documentation](sdk/README.md)
- [Examples](sdk/examples/)

## API Access

For API access and pricing information, contact us.

## License

MIT License - see [LICENSE](LICENSE) for details.

---

**VAP** - Visual Asset Production Engine
