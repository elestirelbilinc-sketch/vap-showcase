# VAP Media · Unified MCP Server for AI Agents (Flux · Veo · Suno)

**Generate AI images, videos, and music with deterministic pricing.**
[![MCP Badge](https://lobehub.com/badge/mcp/elestirelbilinc-sketch-vap-showcase)](https://lobehub.com/mcp/elestirelbilinc-sketch-vap-showcase)
[![MCP Registry](https://img.shields.io/badge/MCP-Registry-blue)](https://registry.modelcontextprotocol.io)
[![Version](https://img.shields.io/badge/version-1.13.0-blue.svg)](https://github.com/vapagentmedia/vap-showcase/releases)
[![Python](https://img.shields.io/badge/python-3.11+-green.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-yellow.svg)](LICENSE)
[![Get Started](https://img.shields.io/badge/Get%20Started-Dashboard-6366f1)](https://vapagent.com/dashboard/signup.html)

---

## Get Started

**No setup required – start generating in 2 minutes:**

1. **[Create Agent](https://vapagent.com/dashboard/signup.html)** → Get your API key instantly
2. **[Add Funds](https://vapagent.com/dashboard/deposit.html)** → Start from $1
3. **Generate** → Start creating images, videos, and music

---

## Why VAP?

VAP is an MCP server that enables image, video, and music generation directly from agentic workflows. It exposes generative media capabilities as portable, pay-per-use tools usable across Claude Desktop, Cursor, and other MCP-compatible clients.

When AI agents work with paid APIs, they need:

- **Cost visibility** – Know exactly what you'll pay before execution
- **Retry control** – Bounded, predictable retry behavior
- **Clear ownership** – Every task tracked and accountable
- **Enterprise auth** – OAuth 2.1 M2M for secure integrations

VAP provides this control layer.

---

## What VAP Does

VAP is an **MCP Server** that provides **Flux image generation**, **Veo 3.1 video generation**, and **Suno V5 music generation** with full cost control.

**Supported AI Models:**
- **Flux2 Pro** – Photorealistic images
- **Veo 3.1** – Cinematic videos
- **Suno V5** – Original music

**Production Pipeline:**
- FFmpeg post-processing (format conversion, audio normalization)
- Automatic quality optimization for broadcast standards
- Permanent cloud storage with instant CDN delivery
- Aspect ratio auto-detection from prompt (e.g. "16:9 landscape" → correct dimensions)

**How it works:**
- **Pre-commit pricing** – Know exact cost before execution
- **Reserve → Burn → Refund** – Hard budget guarantees
- **Deterministic behavior** – Predictable results every time
- **Explicit ownership** – Every task has a clear owner

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

## Try It Free

Generate an image with zero signup — no API key, no deposit:

```bash
curl -X POST https://api.vapagent.com/v3/trial/generate \
  -H "Content-Type: application/json" \
  -d '{"prompt": "A mountain landscape at sunset, photorealistic"}'
```

Rate limit: 3 images per day per IP.

Ready for more? Create an agent below.

---

## MCP Integration

### Step 1: Get Your API Key

**Option A: Dashboard (Recommended)**

Go to **[vapagent.com/dashboard/signup.html](https://vapagent.com/dashboard/signup.html)** and create your agent.

**Option B: API**

```bash
curl -X POST https://api.vapagent.com/v3/agents \
  -H "Content-Type: application/json" \
  -d '{"Name": "my-agent"}'
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
|------|-------------|
| `generate_image` | Create AI image from text prompt |
| `generate_video` | Create cinematic video from text (Veo 3.1) |
| `generate_music` | Create original music from text (Suno V5) |
| `upscale` | Upscale image resolution (2x/4x) |
| `background_remove` | Remove image background |
| `inpaint` | Edit specific regions of an image |
| `video_trim` | Trim video to specific time range |
| `video_merge` | Merge multiple video clips |
| `estimate_cost` | Preview image generation cost |
| `estimate_video_cost` | Preview video generation cost |
| `estimate_music_cost` | Preview music generation cost |
| `check_balance` | Check your current balance |
| `get_task` | Check status of a generation task |
| `get_operation` | Check status of an edit operation |
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

## OAuth 2.1 (Enterprise)

For enterprise integrations, VAP supports OAuth 2.1 M2M (machine-to-machine) authentication via [Scalekit](https://scalekit.com).

### How It Works

```
OAuth Token → MCP Proxy → Validate → Resolve client_id → Agent → Execute
```

### Setup

```bash
# 1. Get OAuth token from your identity provider
curl -X POST "https://your-tenant.scalekit.dev/oauth/token" \
  -d "grant_type=client_credentials" \
  -d "client_id=m2m_xxx" \
  -d "client_secret=your_secret"

# 2. Link OAuth client to your VAP agent (one-time)
curl -X PUT "https://api.vapagent.com/v3/agents/me/oauth" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"oauth_client_id": "m2m_xxx"}'

# 3. Use OAuth token with MCP
# The MCP proxy validates tokens and maps to linked agents
```

### Benefits

- **SSO Integration** – Connect VAP to your existing identity provider
- **No API Key in Config** – Tokens rotate automatically
- **Audit Trail** – OAuth events logged separately

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
| `/v3/agents` | POST | Register new agent |
| `/v3/agents/me/balance` | GET | Check account balance |
| `/v3/agents/me/oauth` | PUT | Link OAuth client (Enterprise) |
| `/v3/agents/me/oauth` | GET | Check OAuth link status |
| `/v3/tasks` | POST | Create media generation task |
| `/v3/tasks/{id}` | GET | Retrieve task status |
| `/v3/execute` | POST | Execute preset (campaign/production) |
| `/v3/operations` | POST | Run edit operation (upscale, bg_remove, etc.) |
| `/v3/operations/{id}` | GET | Check operation status |
| `/v3/deposits/init` POST | Initialize deposit |
| `/v3/trial/generate` | POST | Free trial image (no auth) |
| `/mcp` | - | MCP streamable-http endpoint |

**Full API Docs:** [vapagent.com/quick-start.html](https://vapagent.com/quick-start.html)

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
- **API Documentation:** [vapagent.com/quick-start.html](https://vapagent.com/quick-start.html)
- **MCP Endpoint:** `https://api.vapagent.com/mcp`

---

## License

MIT License – see the [LICENSE](LICENSE) file for details.

---

**VAP Media · Unified MCP Server for AI Agents**

*"Deterministic media production for AI agents."*

## Hosted deployment

A hosted deployment is available on [Fronteir AI](https://fronteir.ai/mcp/elestirelbilinc-sketch-vap-showcase).

