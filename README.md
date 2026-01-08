VAP – Media Execution Engine

# VAP – Media Execution Engine

AI-powered media execution for autonomous agents.

![Version](https://img.shields.io/badge/version-1.6.0-blue.svg)
![Python](https://img.shields.io/badge/python-3.11+-green.svg)
![License](https://img.shields.io/badge/license-MIT-yellow.svg)

## Overview

VAP is a **media execution engine** for autonomous agents.  
It orchestrates image, video, and other media generation tasks as controlled, production-grade executions rather than single-shot requests.

The system is designed to support multiple media providers and protocols under a unified execution surface.

---

## Features

- **Media Execution** – Task-based execution for AI-generated media
- **Image Generation** – High-quality AI image production
- **Video Generation** – AI-powered video execution
- **Multi-Protocol Support** – REST API, A2A Protocol, MCP Server
- **Production Ready** – Built for reliable, long-running workloads

---

## Quick Start

### Installation

```bash
pip install vape-client
Basic Usage
python
Kodu kopyala
from vape_client import VAPClient

client = VAPClient(api_key="your_api_key")

result = client.generate_image(
    prompt="A serene mountain landscape at sunset"
)

print(f"Image URL: {result.url}")
Async Usage
python
Kodu kopyala
import asyncio
from vape_client import AsyncVAPClient

async def main():
    client = AsyncVAPClient(api_key="your_api_key")
    result = await client.generate_image(
        prompt="A futuristic cityscape"
    )
    print(f"Image URL: {result.url}")

asyncio.run(main())
API Endpoints
Endpoint	Method	Description
/v3/generate	POST	Create media execution task
/v3/tasks/{id}	GET	Retrieve task status
/v3/tasks/{id}/result	GET	Retrieve task result

MCP Server
VAP supports the Model Context Protocol (MCP) for integration with Claude Desktop and other MCP-compatible clients.

json
Kodu kopyala
{
  "mcpServers": {
    "vap": {
      "url": "https://api.vapagent.com/mcp"
    }
  }
}
Documentation
API Reference

SDK Documentation

Examples

API Access
For API access and pricing information, please contact us.

License
MIT License – see the LICENSE file for details.

---

VAP – Media Execution Engine
