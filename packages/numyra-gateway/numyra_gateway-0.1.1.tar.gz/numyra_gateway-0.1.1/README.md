# Numyra Gateway

A proxy gateway for intercepting and analyzing Anthropic Claude API streaming responses using mitmproxy.

## Features

- **SSE Stream Parsing**: Parse Server-Sent Events from Claude API responses
- **Anthropic Message Reconstruction**: Rebuild streaming messages from SSE chunks
- **Tool Use Support**: Handle both text and tool use responses with JSON pretty-printing
- **mitmproxy Integration**: Visual inspection of streaming responses in mitmproxy web interface
- **Custom Content Views**: Dedicated "Numyra Anthropic View" for formatted message display

## Installation

```bash
pip install numyra-gateway
```

## Usage

### Command Line

Start the gateway proxy:

```bash
numyra-gateway
```

This will start:
- Proxy server on `http://127.0.0.1:8080` (reverse proxy to `https://api.anthropic.com`)
- Web interface on `http://127.0.0.1:8081`

### Python API

```python
from numyra_gateway.streaming import AnthropicStreamParser

# Parse streaming SSE responses
parser = AnthropicStreamParser()
message = parser.feed(sse_content)

if message and message.is_complete:
    print(f"Content: {message.content}")
    print(f"Stop reason: {message.stop_reason}")
```

## Requirements

- Python 3.13+
- mitmproxy 12.1.2+

## Development

```bash
# Install with dev dependencies
uv sync --group dev

# Run tests
uv run pytest

# Start development server
uv run numyra-gateway
```

## License

**PROPRIETARY SOFTWARE - NOT FREE TO USE**

This is a development version owned by Numyra and is NOT free to use. This software is provided for evaluation and development purposes only. Commercial use is strictly prohibited without explicit written permission from Numyra. See LICENSE file for complete terms.