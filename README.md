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
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
   You must set up the following environment variables either in your `.env` file or in your virtual environment:

   ```bash
   # Required for Claude API
   export ANTHROPIC_API_KEY=your_anthropic_api_key

   # Required for RisingWave connection
   export RISINGWAVE_HOST=0.0.0.0
   export RISINGWAVE_PORT=4566
   export RISINGWAVE_USER=root
   export RISINGWAVE_PASSWORD=root
   export RISINGWAVE_SSLMODE=disable
   export RISINGWAVE_TIMEOUT=30
   ```

   Or create a `.env` file in the root directory:
   ```
   ANTHROPIC_API_KEY=your_anthropic_api_key
   RISINGWAVE_HOST=your_risingwave_host
   RISINGWAVE_PORT=your_risingwave_port
   RISINGWAVE_USER=your_risingwave_user
   RISINGWAVE_PASSWORD=your_risingwave_password
   ```

   ⚠️ Important: The application will not work without these environment variables properly set.

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

## Troubleshooting

If you encounter connection issues:
1. Verify all environment variables are set correctly
2. Check that RisingWave is running and accessible
3. Ensure your Anthropic API key is valid
4. Check the logs for specific error messages

## License

This project is licensed under the MIT License - see the LICENSE file for details. 
