# RisingWave Agent Demo

## Overview
This project demonstrates the use of a RisingWave agent for interacting with a RisingWave streaming database. It includes tools for running queries, generating data, and more.

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
- `risingwave-agent.py`: Main entry point for the agent
- `client.py`: Client implementation for MCP communication

## Data Generator
A sample data generator script is provided at `data-generator.py`. This script continuously generates synthetic user, transaction, and risk score data and inserts it into a RisingWave-compatible PostgreSQL database. It is useful for simulating a real-time data stream for testing and demo purposes.

### How to Use the Data Generator
1. **Install dependencies:**
   - Make sure you have `psycopg2` installed: `pip install psycopg2`
2. **Set up your RisingWave/PostgreSQL instance:**
   - The script connects to the database using the following default parameters:
     - dbname: `dev`
     - user: `root`
     - password: (empty)
     - host: `localhost`
     - port: `4566`
   - You can modify these in the script if needed.
3. **Create the required tables:**
   - Before running the data generator, create the following tables in your database:

```sql
CREATE TABLE users (
  user_id INT PRIMARY KEY,
  full_name TEXT,
  signup_date TIMESTAMP,
  country TEXT
);

CREATE TABLE transactions (
  transaction_id BIGINT PRIMARY KEY,
  user_id INT,
  amount FLOAT,
  transaction_type TEXT,
  merchant_name TEXT,
  device_type TEXT,
  location TEXT,
  timestamp TIMESTAMP
);

CREATE TABLE user_risks (
  risk_id BIGINT PRIMARY KEY,
  user_id INT,
  risk_score FLOAT,
  timestamp TIMESTAMP
);
```

4. **Run the data generator:**
   - Run the script:
     ```bash
     python data-generator.py
     ```
   - The script will continuously insert new users, transactions, and risk scores into the database.

5. **Stop the generator:**
   - Press `Ctrl+C` to stop the script. It will close the database connection gracefully.

For more information, see the RisingWave documentation at [https://risingwave.dev](https://risingwave.dev)

## Troubleshooting

If you encounter connection issues:
1. Verify all environment variables are set correctly
2. Check that RisingWave is running and accessible
3. Ensure your Anthropic API key is valid
4. Check the logs for specific error messages
