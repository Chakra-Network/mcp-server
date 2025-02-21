import os
from typing import Any, Optional

import requests
from chakra_py import Chakra
from mcp.server.fastmcp import FastMCP

from consts import PROMPT_TEMPLATE

server = FastMCP("chakra")


class ChakraConnectionManager:
    """
    Manages the connection to Chakra.
    """

    def __init__(self, db_session_key: str):
        self.client: Optional[Chakra] = None
        self.db_session_key = db_session_key

    def initialize_connection(self) -> str:
        """
        Initializes connection to Chakra.
        """
        self.client = Chakra(
            self.db_session_key,
            quiet=True,
        )
        self.client.login()
        return "Connection successfully created!"

    # TODO: MOVE INTO PYTHON SDK
    def _fetch_db_list(token) -> list[str]:
        url = "https://api.chakra.dev/api/v1/databases"

        headers = {"Authorization": f"Bearer {token}"}
        response = requests.request("GET", url, headers=headers)

        return response.json()["databases"]

    # TODO: MOVE INTO PYTHON SDK
    def _fetch_db_metadata(db_list: list[str], token: str) -> list[str]:
        metadata = []
        for db in db_list:
            url = f"https://api.chakra.dev/api/v1/databases/{db}"
            headers = {"Authorization": f"Bearer {token}"}
            response = requests.request("GET", url, headers=headers)
            metadata.append(response.json())

        return metadata

    def is_connected(self) -> bool:
        return self.client is not None and self.client.token is not None

    def execute_query(self, query: str) -> str:
        if not self.is_connected():
            return "Error: connection was never initialized. Try initialize_connection first."
        df = self.client.execute(query)
        return df.to_string()

    def retrieve_database_metadata(self) -> str:
        if not self.is_connected():
            return "Error: connection was never initialized. Try initialize_connection first."
        db_list = ChakraConnectionManager._fetch_db_list(self.client.token)
        metadata = ChakraConnectionManager._fetch_db_metadata(
            db_list, self.client.token
        )
        return str(metadata)


db_session_key = os.getenv("db_session_key")

if not db_session_key:
    raise ValueError(
        "The variable db_session_key is not set. Please set it in your environment variables."
    )

connection_manager = ChakraConnectionManager(db_session_key)


# TODO: WRAP DB METADATA INTO THIS - no need for multiple tools
@server.tool()
def initialize_connection() -> str:
    """
    Initializes connection to Chakra and provides the user with the database metadata.
    """
    connection_manager.initialize_connection()
    return connection_manager.retrieve_database_metadata()


@server.tool()
def execute_query(query: str) -> str:
    """
    Executes a query on the database.
    Make sure that you lower case the text and the column compared and use the LIKE operator. This is very important.
    """
    return connection_manager.execute_query(query)


@server.prompt()
def prompt() -> str:
    """
    A prompt to initialize a connection to Chakra and start working with it
    """
    return PROMPT_TEMPLATE


if __name__ == "__main__":
    server.run(transport="stdio")
