# Chakra MCP Server

[![PyPI version](https://badge.fury.io/py/chakra-mcp.svg)](https://badge.fury.io/py/chakra-mcp)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python versions](https://img.shields.io/pypi/pyversions/chakra-mcp.svg)](https://pypi.org/project/chakra-mcp/)

![mcp](https://github.com/user-attachments/assets/2c9e2b54-2691-43c7-928b-bd6e33cc5f73)


A native integration with Anthropic's [Model Context Protocol (MCP)](https://www.anthropic.com/news/model-context-protocol). Allows you to interact with your database and subscribed data shares using natural language.

## Features
- **Natural Language Queries**: Query your database using natural language.
- **Data Share Interactions**: Interact with subscribed data shares. For example, if you have subscribed to a financial data share, you can ask questions like "What is the stock price of Tesla?"
- **Database Management**: Create, update, and delete tables.

## Demo
https://github.com/user-attachments/assets/0d1b3588-4dec-4fae-8396-d1794177a23c

## Prerequisites
- Python 3.11+
- [pip](https://pip.pypa.io/en/stable/installation/)
- Chakra Account - sign up [here](https://console.chakra.dev/)

## Finding your DB Session Key

1. Login to the [Chakra Console](https://console.chakra.dev/)
2. Select Settings
3. Navigate to the releveant database and copy the DB Session Key (not the access key or secret access key)

https://github.com/user-attachments/assets/9f1c1ab8-cb87-42a1-8627-184617bbb7d7

## Installation

### Automated Using OpenTools (Easier)

TBD

### Manual Setup (More Work)

Clone the repository by running:
```bash
pip install chakra-mcp
```

Add the following to your `claude_desktop_config.json` file:
- On MacOS: `~/Library/Application\ Support/Claude/claude_desktop_config.json`
- On Windows: `%APPDATA%/Claude/claude_desktop_config.json`

```json
{
  "mcpServers": {
     "chakra": {
      "command": "python",
      "args": [
        "-m",
        "chakra_mcp"
      ],
      "env": {
        "db_session_key": "YOUR_DB_SESSION_KEY"
      }
    }
  }
}
```

## Architecture

<img width="1004" alt="architecture" src="https://github.com/user-attachments/assets/0984e717-afc5-4599-b2c0-eefa33d40441" />

## Disclaimers 

- MCP is extremely early. The experience in Claude Desktop is suboptimal - every time you use the server, you have to grant access explicitly. This is a design decision on Anthropic's part and is not yet configurable.
- Setup is rough around the edges. We have worked closely with the folks at OpenTools to make this as seamless as possible, but there is room for improvement. We are looking forward to an MCP GUI experience in the future, but for now, users must use the command-line. 
- Today, the server runs on the user's local machine. Anthropic's roadmap includes a [hosted server option](https://modelcontextprotocol.io/development/roadmap#remote-mcp-support), which we will support. This will make authentication, setup, and performance much better. 

## License

MIT License - see LICENSE file for details.

## Support

For support and questions, please open an issue in the GitHub repository or reach out to us on [Discord](https://discord.gg/chakra-ai).
