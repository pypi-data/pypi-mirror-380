# MiMiMON

**AI Agent Monitoring and Communication Platform**

MiMiMON is a comprehensive toolkit for monitoring, communicating with, and managing AI agents across multiple platforms and environments.

## Features

- 🔍 **Agent Monitoring**: Real-time monitoring of AI agents
- 💬 **Remote Communication**: Communicate with agents from anywhere
- 🌐 **Multi-Platform Support**: Works with Claude, GPT, and other AI agents
- 🔧 **MCP Support**: Model Context Protocol integration
- 📱 **Cross-Platform**: CLI, web dashboard, and mobile app
- 🔄 **Real-time Updates**: WebSocket-based live updates

## Installation

```bash
pip install mimimon
```

## Quick Start

### 1. Start Monitoring

```bash
# Start basic monitoring
mimimon

# Monitor specific agent
mimimon --agent claude

# Enable git diff tracking
mimimon --git-diff
```

### 2. Server Mode

```bash
# Start MiMiMON server
mimimon serve

# Custom host and port
mimimon serve --host 0.0.0.0 --port 8080
```

### 3. MCP Integration

```bash
# Start MCP session
mimimon mcp

# Custom MCP endpoint
mimimon mcp --endpoint ws://localhost:8080/mcp
```

## Commands

- `mimimon` - Start agent monitoring session
- `mimimon serve` - Start backend server
- `mimimon mcp` - Start MCP session
- `mimimon version` - Show version information
- `mimimon status` - Check system status

## Configuration

MiMiMON can be configured using environment variables or command-line options:

- `MIMIMON_API_KEY` - API key for authentication
- `MIMIMON_BASE_URL` - Custom API endpoint
- `MIMIMON_DEBUG` - Enable debug mode

## API Usage

```python
from mimimon import MiMiMONClient

# Initialize client
client = MiMiMONClient(api_key="your_api_key")

# Start monitoring session
session_id = client.start_monitoring_session(agent="claude")

# Send message to agent
await client.send_message(session_id, "Hello, agent!")

# Get session history
history = await client.get_session_history(session_id)
```

## Development

### Installation for Development

```bash
git clone https://github.com/mimimon-ai/mimimon.git
cd mimimon
pip install -e ".[dev]"
```

### Running Tests

```bash
pytest
```

### Code Formatting

```bash
black mimimon/
ruff check mimimon/
```

## License

MIT License - see LICENSE file for details.

## Links

- 🌐 [Website](https://mimimon.ai)
- 📖 [Documentation](https://docs.mimimon.ai)
- 🐙 [GitHub](https://github.com/mimimon-ai/mimimon)
- 📱 [Mobile App](https://apps.apple.com/app/mimimon)
- 🖥️ [Web Dashboard](https://dashboard.mimimon.ai)