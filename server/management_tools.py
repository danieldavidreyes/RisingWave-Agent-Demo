from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

from fastmcp import FastMCP
from risingwave import OutputFormat
from connection import setup_risingwave_connection


def register_management_tools(mcp: FastMCP):
    """Register all database management MCP tools"""

    @mcp.tool
    def get_database_version() -> str:
        """
        Get the RisingWave database version information.

        Returns:
            Database version information
        """
        rw = setup_risingwave_connection()
        result = rw.fetchone("SELECT version()", format=OutputFormat.DATAFRAME)
        return result

    @mcp.tool
    def show_running_queries() -> str:
        """
        Show currently running queries (if supported by RisingWave version).

        Returns:
            List of running queries or error message
        """
        rw = setup_risingwave_connection()
        try:
            # This may not be available in all RisingWave versions
            result = rw.fetch("SHOW PROCESSLIST",
                              format=OutputFormat.DATAFRAME)
            return result
        except Exception as e:
            return f"Show running queries not supported or error occurred: {str(e)}"

    @mcp.tool
    def flush_database() -> str:
        """
        Force flush all pending writes to the database.

        Returns:
            Success message
        """
        rw = setup_risingwave_connection()
        try:
            rw.execute("FLUSH")
            return "Database flush completed successfully"
        except Exception as e:
            return f"Error flushing database: {str(e)}"
