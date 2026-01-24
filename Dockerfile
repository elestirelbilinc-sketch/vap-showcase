# VAP MCP Server - HTTP Mode for Glama.ai
#
# This Dockerfile creates an HTTP-mode MCP server for inspection by Glama.ai
# and other MCP discovery tools.
#
# Build: docker build -t vap-mcp .
# Run:   docker run -p 8000:8000 vap-mcp
#
# Directive: #549 (HTTP Mode for Glama)

FROM python:3.11-slim

LABEL org.opencontainers.image.title="VAP MCP Server"
LABEL org.opencontainers.image.description="MCP server for AI media generation (image, video, music)"
LABEL org.opencontainers.image.vendor="VAP"
LABEL org.opencontainers.image.url="https://vapagent.com"

WORKDIR /app

# Install dependencies
RUN pip install --no-cache-dir httpx

# Copy MCP proxy
COPY mcp/vap_mcp_proxy.py .

# Expose HTTP port
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/health')" || exit 1

# Run in HTTP mode for Glama inspection
ENTRYPOINT ["python", "vap_mcp_proxy.py"]
CMD ["--mode=http", "--port=8000"]
