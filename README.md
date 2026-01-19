# VAP – Execution Control Layer for AI Agents

**"VAP is where nondeterminism stops."**
[![MCP Badge](https://lobehub.com/badge/mcp/elestirelbilinc-sketch-vap-showcase)](https://lobehub.com/mcp/elestirelbilinc-sketch-vap-showcase)
[![MCP Registry](https://img.shields.io/badge/MCP-Registry-blue)](https://registry.modelcontextprotocol.io)
[![Version](https://img.shields.io/badge/version-1.12.4-blue.svg)](https://github.com/elestirelbilinc-sketch/vap-showcase/releases)
[![Python](https://img.shields.io/badge/python-3.11+-green.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-yellow.svg)](LICENSE)

---

## The Problem

If your agents call paid APIs directly, you don't have:
- **Cost control** – No budget limits, no spending caps
- **Retry limits** – Failed calls can loop indefinitely
- **Failure ownership** – No clear accountability when things go wrong

Your AI agent needs to generate an image. It calls DALL-E. The call fails. It retries. Fails again. Retries 10 more times.

**You just burned $5 on nothing.**

---

## The Solution

VAP is an **Execution Control Layer** that sits between AI agents and paid external APIs.

It enforces:
- **Pre-commit pricing** – Know exact cost before execution
- **Hard budget guarantees** – Reserve → Burn → Refund model
- **Deterministic retry behavior** – No runaway costs
- **Explicit execution ownership** – Every task has an owner

---

## How It Works

```
Agent: "Generate an image of a sunset"
    ↓
VAP: "That will cost $0.18. Reserving..."
VAP: "Reserved. Executing..."
VAP: "Success. Burning $0.18. Here's your image."
```

If it fails:

```
Agent: "Generate an image of a sunset"
    ↓
VAP: "That will cost $0.18. Reserving..."
VAP: "Reserved. Executing..."
VAP: "Failed. Refunding $0.18. Error: Provider timeout"
```

**Your agent never sees the complexity. It just gets deterministic results.**

---

## Pricing

| Type | Preset | Price |
|------|--------|-------|
| Image(Photorealistic) | `image.basic` | **$0.18** |
| Video(VEO3.1 | `video.basic` | **$1.96** |
| Music(SUNO V5) | `music.basic` | **$0.68** |
| Campaign | `streaming_campaign` | **$5.90** |
| Full Production | `full_production` | **$7.90** |

No surprises. No variable pricing. No "it depends."
All media productions are automatically normalized and delivered through a fast, orchestrated pipeline in accordance with defined broadcast quality standards.
---

## MCP Integration

VAP is on the official **MCP Registry**: `io.github.elestirelbilinc-sketch/vap-e`

### Claude Desktop Configuration

```json
{
  "mcpServers": {
    "vap": {
      "url": "https://api.vapagent.com/mcp",
      "transport": "streamable-http"
    }
  }
}
```

### Available Tools (10)

| Tool | Description |
|------|-------------|
| `generate_image` | Generate AI image ($0.18) |
| `generate_video` | Generate AI video(Veo3.1) ($1.96) |
| `generate_music` | Generate AI music(SunoV5) ($0.68) |
| `estimate_cost` | Get image generation cost |
| `estimate_video_cost` | Get video generation cost |
| `estimate_music_cost` | Get music generation cost |
| `check_balance` | Check account balance |
| `get_task` | Get task status by ID |
| `list_tasks` | List recent tasks |
| `execute_preset` | Execute named preset |

---

## SDK Usage

### Installation

```bash
pip install vape-client
```

### Basic Usage

```python
from vape_client import VAPClient

client = VAPClient(api_key="your_api_key")

# Cost is pre-committed: $0.18
result = client.generate_image(
    prompt="A serene mountain landscape at sunset"
)

print(f"Image URL: {result.url}")
print(f"Cost: ${result.cost}")
```

### Async Usage

```python
import asyncio
from vape_client import AsyncVAPClient

async def main():
    client = AsyncVAPClient(api_key="your_api_key")

    # Budget enforced, retries limited
    result = await client.generate_image(
        prompt="A futuristic cityscape"
    )
    print(f"Image URL: {result.url}")

asyncio.run(main())
```

---

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/v3/generate` | POST | Create media execution task |
| `/v3/tasks/{id}` | GET | Retrieve task status |
| `/v3/tasks/{id}/result` | GET | Retrieve task result |
| `/v3/balance` | GET | Check account balance |

**Full API Docs:** [api.vapagent.com/docs](https://api.vapagent.com/docs)

---

## The Three Guarantees

### 1. Pre-Commit Pricing
Every task has a known cost before execution. No surprises.

### 2. Budget Enforcement
Set a max budget. VAP enforces it. Hit the limit? Task rejected. Balance protected.

### 3. Failure Ownership
Every task has an explicit owner. Every failure has an address. No more "the agent did something and I don't know what."

---

## Links

- **MCP Registry:** [registry.modelcontextprotocol.io](https://registry.modelcontextprotocol.io)
- **API Documentation:** [api.vapagent.com/docs](https://api.vapagent.com/docs)
- **MCP Endpoint:** `https://api.vapagent.com/mcp`

---

## License

MIT License – see the [LICENSE](LICENSE) file for details.

---

**VAP – Execution Control Layer for AI Agents**

*"VAP is where nondeterminism stops."*
