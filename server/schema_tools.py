from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

from fastmcp import FastMCP
from risingwave import OutputFormat
from connection import setup_risingwave_connection


def register_schema_tools(mcp: FastMCP):
    """Register all schema-related MCP tools"""

    @mcp.tool
    def show_tables() -> str:
        """List all tables in the database."""
        rw = setup_risingwave_connection()
        result = rw.fetch("SHOW TABLES", format=OutputFormat.DATAFRAME)
        return result

    @mcp.tool
    def list_databases() -> str:
        """List all databases in the RisingWave cluster."""
        rw = setup_risingwave_connection()
        result = rw.fetch("SHOW DATABASES", format=OutputFormat.DATAFRAME)
        return result

    @mcp.tool
    def describe_table(table_name: str) -> str:
        """
        Describe the structure of a table (columns, types, etc.).

        Args:
            table_name: Name of the table to describe

        Returns:
            Table structure information
        """
        rw = setup_risingwave_connection()
        query = f"DESCRIBE {table_name}"
        result = rw.fetch(query, format=OutputFormat.DATAFRAME)
        return result

    @mcp.tool
    def describe_materialized_view(mv_name: str) -> str:
        """
        Describe the structure of a materialized view (columns, types, etc.).

        Args:
            mv_name: Name of the table to describe

        Returns:
            Table structure information
        """
        rw = setup_risingwave_connection()
        query = f"DESCRIBE {mv_name}"
        result = rw.fetch(query, format=OutputFormat.DATAFRAME)
        return result

    @mcp.tool
    def show_create_table(table_name: str) -> str:
        """
        Show the CREATE TABLE statement for a specific table.

        Args:
            table_name: Name of the table

        Returns:
            CREATE TABLE statement
        """
        rw = setup_risingwave_connection()
        query = f"SHOW CREATE TABLE {table_name}"
        result = rw.fetch(query, format=OutputFormat.DATAFRAME)
        return result

    @mcp.tool
    def show_create_materialized_view(mv_name: str) -> str:
        """
        Show the CREATE MATERIALIZED VIEW statement for a specific materialized view.

        Args:
            mv_name: Name of the materialized view

        Returns:
            CREATE MATERIALIZED VIEW statement
        """
        rw = setup_risingwave_connection()
        query = f"SHOW CREATE MATERIALIZED VIEW {mv_name}"
        result = rw.fetch(query, format=OutputFormat.DATAFRAME)
        return result

    @mcp.tool
    def check_table_exists(table_name: str, schema_name: str = "public") -> str:
        """
        Check if a table or materialized view exists in the specified schema.

        Args:
            table_name: Name of the table to check
            schema_name: Name of the schema (default: "public")

        Returns:
            Boolean result as string indicating if table exists
        """
        rw = setup_risingwave_connection()
        exists = rw.check_exist(name=table_name, schema_name=schema_name)
        return f"Table '{table_name}' in schema '{schema_name}' exists: {exists}"

    @mcp.tool
    def list_schemas() -> str:
        """
        List all schemas in the RisingWave database.

        Returns:
            List of schemas as a formatted string
        """
        rw = setup_risingwave_connection()
        result = rw.fetch(
            "SELECT schema_name FROM information_schema.schemata", format=OutputFormat.DATAFRAME)
        return result

    @mcp.tool
    def list_materialized_views() -> str:
        """
        List all materialized views in a specific schema.

        Args:
            schema_name: Name of the schema (default: "public")

        Returns:
            List of materialized views
        """
        rw = setup_risingwave_connection()
        query = "SHOW MATERIALIZED VIEWS"
        result = rw.fetch(query, format=OutputFormat.DATAFRAME)
        return result

    @mcp.tool
    def get_table_columns(table_name: str, schema_name: str = "public") -> str:
        """
        Get detailed column information for a table.

        Args:
            table_name: Name of the table
            schema_name: Name of the schema (default: "public")

        Returns:
            Column details including names, types, and constraints
        """
        rw = setup_risingwave_connection()
        query = f"""
        SELECT column_name, data_type, is_nullable, column_default
        FROM information_schema.columns 
        WHERE table_name = '{table_name}' AND table_schema = '{schema_name}'
        ORDER BY ordinal_position
        """
        result = rw.fetch(query, format=OutputFormat.DATAFRAME)
        return result

    @mcp.tool
    def list_subscriptions(schema_name: str = "public") -> str:
        """
        List all subscriptions in a specific schema.

        Args:
            schema_name: Name of the schema (default: "public")

        Returns:
            List of subscriptions
        """
        rw = setup_risingwave_connection()
        query = f"SHOW SUBSCRIPTIONS FROM {schema_name}"
        try:
            result = rw.fetch(query, format=OutputFormat.DATAFRAME)
            return result
        except Exception as e:
            return f"Error listing subscriptions: {str(e)}"

    @mcp.tool
    def list_table_privileges(table_name: str, schema_name: str = "public") -> str:
        """
        List privileges for a specific table.

        Args:
            table_name: Name of the table
            schema_name: Name of the schema (default: "public")

        Returns:
            Table privileges information
        """
        rw = setup_risingwave_connection()
        query = f"""
        SELECT grantee, privilege_type, is_grantable
        FROM information_schema.table_privileges 
        WHERE table_name = '{table_name}' AND table_schema = '{schema_name}'
        """
        try:
            result = rw.fetch(query, format=OutputFormat.DATAFRAME)
            return result
        except Exception as e:
            return f"Error getting table privileges: {str(e)}"
