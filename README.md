# RisingWave Agent Demo

A demonstration of using Claude AI with RisingWave database through MCP (Model Control Protocol) tools.

## Prerequisites

- Python 3.8 or higher
- RisingWave database instance
- Anthropic API key

## Setup

1. Clone this repository:
```bash
git clone <your-repo-url>
cd risingwave-agent-demo
```

2. Clone the RisingWave MCP server:
```bash
git clone https://github.com/risingwavelabs/risingwave-mcp.git
cp -r risingwave-mcp/src/* server/
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the root directory with your credentials:
```
ANTHROPIC_API_KEY=your_anthropic_api_key
RISINGWAVE_HOST=your_risingwave_host
RISINGWAVE_PORT=your_risingwave_port
RISINGWAVE_USER=your_risingwave_user
RISINGWAVE_PASSWORD=your_risingwave_password
```

## Usage

1. Start RisingWave:
```bash
risingwave
```

2. In a new terminal, run the agent:
```bash
python risingwave-agent.py
```

3. The agent will start an interactive session where you can ask questions about your RisingWave database.

## Features

- Natural language interface to RisingWave database
- Support for SQL queries, schema management, and database operations
- Real-time database interaction through MCP tools
- Powered by Claude AI for intelligent responses

## Project Structure

- `agents/`: Agent implementation with Claude API integration
- `server/`: RisingWave MCP server implementation (cloned from risingwave-mcp)
- `risingwave-agent.py`: Main entry point for the agent
- `client.py`: Client implementation for MCP communication

## License

This project is licensed under the MIT License - see the LICENSE file for details. 