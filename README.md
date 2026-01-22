# VAP Media · Unified MCP Server for AI Agents (Flux · Veo · Suno)

**Generate AI images, videos, and music with deterministic pricing.**
[![MCP Badge](https://lobehub.com/badge/mcp/elestirelbilinc-sketch-vap-showcase)](https://lobehub.com/mcp/elestirelbilinc-sketch-vap-showcase)
[![MCP Registry](https://img.shields.io/badge/MCP-Registry-blue)](https://registry.modelcontextprotocol.io)
[![Version](https://img.shields.io/badge/version-1.12.4-blue.svg)](https://github.com/elestirelbilinc-sketch/vap-showcase/releases)
[![Python](https://img.shields.io/badge/python-3.11+-green.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-yellow.svg)](LICENSE)
[![Get Started](https://img.shields.io/badge/Get%20Started-Dashboard-6366f1)](https://vapagent.com/dashboard/signup.html)

---

## Get Started

**No setup required – start generating in 2 minutes:**

1. **[Create Agent](https://vapagent.com/dashboard/signup.html)** → Get your API key instantly
2. **[Add Funds](https://vapagent.com/dashboard/deposit.html)** → Crypto (USDT/USDC/BTC/ETH) or Card (coming soon)
3. **Generate** → Start creating images, videos, and music

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

VAP is an **MCP Server** that provides **Flux image generation**, **Veo 3.1 video generation**, and **Suno V5 music generation** with cost control.

**Supported AI Models:**
- **Flux2 Pro** – Photorealistic images
- **Veo 3.1** – Cinematic videos
- **Suno V5** – Original music

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
VAP: "Reserving cost..."
VAP: "Reserved. Executing..."
VAP: "Success. Here's your image."
```

If it fails:

```
Agent: "Generate an image of a sunset"
    ↓
VAP: "Reserving cost..."
VAP: "Reserved. Executing..."
VAP: "Failed. Full refund. Error: Provider timeout"
```

**Your agent never sees the complexity. It just gets deterministic results.**

---

## Presets

| Type | Preset |
|------|--------|
| Image | `image.basic` |
| Video | `video.basic` |
| Music | `music.basic` |
| Campaign+SEO | `streaming_campaign` |
| Full Production+SEO | `full_production` |

All media productions are automatically normalized and delivered through a fast, orchestrated pipeline in accordance with defined broadcast quality standards.

**Pricing:** See [vapagent.com](https://vapagent.com) for current pricing.

---

## MCP Integration

### Step 1: Get Your API Key

**Option A: Dashboard (Recommended)**

Go to **[vapagent.com/dashboard/signup.html](https://vapagent.com/dashboard/signup.html)** and create your agent.

**Option B: API**

```bash
curl -X POST https://api.vapagent.com/v3/agents \
  -H "Content-Type: application/json" \
  -d '{"name": "my-agent"}'
```

Save the `api_key` from the response. It's shown only once.

### Step 2: Activate Your Account

Deposit minimum $1 to unlock generation capabilities:

```bash
curl -X POST https://api.vapagent.com/v3/deposits/init \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{"amount": 5.00, "provider": "crypto"}'
```

### Step 3: Configure Your MCP Client

#### Claude Desktop

Add to `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "vap": {
      "url": "https://api.vapagent.com/mcp",
      "transport": "streamable-http",
      "headers": {
        "Authorization": "Bearer YOUR_API_KEY"
      }
    }
  }
}
```

#### Cursor

Add to `.cursor/mcp.json` (project) or `~/.cursor/mcp.json` (global):

```json
{
  "mcpServers": {
    "vap": {
      "command": "npx",
      "args": [
        "mcp-remote",
        "https://api.vapagent.com/mcp",
        "--header",
        "Authorization: Bearer YOUR_API_KEY"
      ]
    }
  }
}
```

#### Cline (VS Code)

Add to Cline MCP settings:

```json
{
  "mcpServers": {
    "vap": {
      "command": "python",
      "args": ["path/to/mcp/vap_mcp_proxy.py"],
      "env": {
        "VAP_API_KEY": "your_api_key"
      }
    }
  }
}
```

Restart your client after configuration.

### Available Tools

| Tool | What it does |
|------|--------------|
| `generate_image` | Create photorealistic image from text (Flux2 Pro) |
| `generate_video` | Create cinematic video from text (Veo 3.1) |
| `generate_music` | Create original music from text (Suno V5) |
| `estimate_cost` | Preview cost before generating |
| `check_balance` | Check your current balance |
| `get_task` | Check status of a running task |
| `list_tasks` | List your recent tasks |

### Alternative: Local Proxy

For environments that don't support `headers`, use the local proxy:

```json
{
  "mcpServers": {
    "vap": {
      "command": "python",
      "args": ["/path/to/mcp/vap_mcp_proxy.py"],
      "env": {
        "VAP_API_KEY": "your_api_key"
      }
    }
  }
}
```

**MCP Registry:** `io.github.elestirelbilinc-sketch/vap-e`

---

## SDK Usage

### Installation

```bash
pip install vap-sdk
```

### Image Generation

```python
from vape_client import VAPEClient

client = VAPEClient(api_key="your_api_key")

result = client.generate(
    description="A serene mountain landscape at sunset"
)

print(f"Image URL: {result.image_url}")
print(f"Cost: ${result.cost}")
```

### Video Generation

```python
# Generate video with Veo 3.1
video = client.generate_video(
    prompt="Cinematic aerial shot of coastal cliffs at golden hour",
    duration=8,
    aspect_ratio="16:9",
    generate_audio=True
)

print(f"Task ID: {video.task_id}")

# Poll for completion
task = client.get_task(video.task_id)
print(f"Status: {task.status}")
print(f"Video URL: {task.result_url}")
```

### Music Generation

```python
# Generate music with Suno V5
music = client.generate_music(
    prompt="Upbeat indie folk song with acoustic guitar and warm vocals",
    duration=120,
    instrumental=False
)

print(f"Task ID: {music.task_id}")

# Check task status
task = client.get_task(music.task_id)
print(f"Audio URL: {task.result_url}")
```

### Async Usage

```python
import asyncio
from vape_client import AsyncVAPEClient

async def main():
    async with AsyncVAPEClient(api_key="your_api_key") as client:
        # Image
        image = await client.generate(description="A futuristic cityscape")
        print(f"Image URL: {image.image_url}")

        # Video
        video = await client.generate_video(prompt="Ocean waves at sunset")
        print(f"Video Task: {video.task_id}")

        # Music
        music = await client.generate_music(prompt="Lo-fi chill beats")
        print(f"Music Task: {music.task_id}")

asyncio.run(main())
```

### Task Management

```python
# List recent tasks
tasks = client.list_tasks(limit=10)
for task in tasks.tasks:
    print(f"{task.task_id}: {task.status} - {task.task_type}")

# Get specific task
task = client.get_task("your-task-id")
print(f"Result: {task.result_url}")
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

## The Four Guarantees

### 1. Pre-Commit Pricing
Every task has a known cost before execution. No surprises.

### 2. Budget Enforcement
Set a max budget. VAP enforces it. Hit the limit? Task rejected. Balance protected.

### 3. Failure Ownership
Every task has an explicit owner. Every failure has an address. No more "the agent did something and I don't know what."

### 4. Deterministic Production Quality
Every output is normalized to broadcast standards. Consistent formats, predictable quality, publish-ready media. No variance between runs.

---

## Links

- **MCP Registry:** [registry.modelcontextprotocol.io](https://registry.modelcontextprotocol.io)
- **API Documentation:** [api.vapagent.com/docs](https://api.vapagent.com/docs)
- **MCP Endpoint:** `https://api.vapagent.com/mcp`

---

## License

MIT License – see the [LICENSE](LICENSE) file for details.

---

**VAP Media · Unified MCP Server for AI Agents**

*"Deterministic media production for AI agents."*
