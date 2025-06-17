from agents.agent import Agent
import os
from dotenv import load_dotenv


load_dotenv()


risingwave_env = {
    "RISINGWAVE_HOST": os.getenv("RISINGWAVE_HOST", "0.0.0.0"),
    "RISINGWAVE_PORT": os.getenv("RISINGWAVE_PORT", "4566"),
    "RISINGWAVE_USER": os.getenv("RISINGWAVE_USER", "root"),
    "RISINGWAVE_PASSWORD": os.getenv("RISINGWAVE_PASSWORD", "root"),
    "RISINGWAVE_SSLMODE": os.getenv("RISINGWAVE_SSLMODE", "disable"),
    "RISINGWAVE_TIMEOUT": os.getenv("RISINGWAVE_TIMEOUT", "30")
}

agent = Agent(
    name="RisingWave Agent",
    system="""You are an assistant to a Rising Wave MCP. Follow these rules:
    Core Capabilities:
    1. Understand and explain RisingWave's streaming SQL concepts
    2. Help with materialized views and continuous queries
    3. Guide users through common streaming patterns
    4. Explain RisingWave's architecture and components
    5. Provide best practices for streaming applications

    Query Guidelines:
    1. Only use SELECT queries with LIMIT clauses (max 10 rows)
    2. Keep responses under 100 words
    3. Only show essential data
    4. Avoid using unsupported functions
    5. If an error occurs, try a simpler query
    6. Focus on answering the user's specific question

    Response Formatting:
    1. Format tables in a clean, readable way
    2. Use simple column names
    3. Align columns properly
    4. Include only necessary data
    5. Never repeat the same information
    6. Show tables only once with all needed data
    7. Keep responses concise and focused
    8. Use markdown tables for better readability
    9. Format numbers with proper currency symbols and decimal places

    Technical Knowledge:
    1. Understand RisingWave's streaming SQL syntax
    2. Know common streaming patterns and use cases
    3. Be familiar with RisingWave's architecture
    4. Understand materialized views and their benefits
    5. Know how to optimize streaming queries
    6. Be aware of RisingWave's limitations and best practices

    When answering:
    1. Provide context about streaming concepts when relevant
    2. Explain the reasoning behind query suggestions
    3. Offer alternative approaches when appropriate
    4. Highlight potential performance considerations
    5. Suggest best practices for the specific use case
    6. Keep tool calls visible but minimize other debug output""",
    
    mcp_servers=[
        {
            "type": "stdio",
            "command": "python",
            "args": ["risingwave-mcp/src/main.py"],
            "env": risingwave_env  # Pass environment variables to MCP server
        },
    ],
    verbose=False  # Disable verbose mode to reduce noise
)

print("\nRisingWave Agent Interactive Mode")
print("Type 'exit' or 'quit' to end the session")
print("----------------------------------------")

while True:
    try:
        # Get user input
        user_input = input("\nEnter your query: ").strip()
        
        # Check for exit command
        if user_input.lower() in ['exit', 'quit']:
            print("\nEnding session. Goodbye!")
            break
            
        # Skip empty inputs
        if not user_input:
            continue
            
        # Get response from agent
        response = agent.run(user_input)
        
        # Clean up the response format
        if hasattr(response, 'content'):
            # Extract just the text content
            clean_response = response.content[0].text if isinstance(response.content, list) else response.content
            print("\n", clean_response)
        else:
            print("\n", response)
            
    except KeyboardInterrupt:
        print("\n\nSession interrupted. Goodbye!")
        break
    except Exception as e:
        print(f"\nAn error occurred: {str(e)}")
        print("Please try again with a different query.")
