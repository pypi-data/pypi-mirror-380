"""Shared MCP tools for both local and remote servers."""

from typing import List, Optional

from mcp.server.fastmcp import Context
from mcp.server.session import ServerSession
from point_topic_mcp.core.context_assembly import list_datasets, assemble_context  
from point_topic_mcp.core.utils import dynamic_docstring



def register_tools(mcp):
    """Register all MCP tools on the provided FastMCP instance."""
    
    @mcp.tool()
    @dynamic_docstring([("{DATASETS}", list_datasets)])
    def assemble_dataset_context(
        dataset_names: List[str], 
        ctx: Optional[Context[ServerSession, None]] = None
    ) -> str:
        """
        Assemble full context (instructions, schema, examples) for one or more datasets.

        This is essential before executing a query, for the agent to understand how to query the datasets.
        
        Args:
            dataset_names: List of dataset names to include (e.g., ['upc', 'upc_take_up'])
        
        {DATASETS}
        
        Returns the complete context needed for querying these datasets.
        """
        # Check if user is authenticated and apply dataset restrictions

        return assemble_context(dataset_names)

    @mcp.tool()
    def execute_query(
        sql_query: str, 
        ctx: Optional[Context[ServerSession, None]] = None
    ) -> str:
        """
        Execute a safe SQL query against the Snowflake database.
        Only read-only queries allowed (SELECT, WITH, SHOW, DESCRIBE, EXPLAIN).
        
        Args:
            sql_query: The SQL query to execute
            
        Returns:
            Query results in CSV format or error message
        """
        from point_topic_mcp.connectors.snowflake import SnowflakeDB

        
        sf = SnowflakeDB()
        sf.connect()
        result = sf.execute_safe_query(sql_query)
        sf.close_connection()
        return result


    @mcp.tool_plain()
    def get_la_code(la_name: str) -> str:
        """
        Get the LA code for a given LA name.

        Args:
            la_name: The name of the LA to get the code for

        Returns:
            The LA code for the given LA name

        Example:
            get_la_code("Westminster") -> "E09000033"
        """
        from point_topic_mcp.connectors.snowflake import SnowflakeDB

        sql_query = f"select distinct la_code from upc_core.reports.upc_output where lower(la_name) like lower('{la_name}')"
        sf = SnowflakeDB()
        sf.connect()
        result = sf.execute_safe_query(sql_query)
        sf.close_connection()
        return result

    @mcp.tool_plain()
    def get_la_list_full(la_name: str) -> str:
        """
        Get the full list of LA codes and names.

        Can be used if the get_la_code tool doesn't match the LA name.

        Returns the full list of LA codes and names in CSV format.
        """
        from point_topic_mcp.connectors.snowflake import SnowflakeDB

        sql_query = f"select distinct la_code, la_name from upc_core.reports.upc_output"
        sf = SnowflakeDB()
        sf.connect()
        result = sf.execute_safe_query(sql_query)
        sf.close_connection()
        return result
