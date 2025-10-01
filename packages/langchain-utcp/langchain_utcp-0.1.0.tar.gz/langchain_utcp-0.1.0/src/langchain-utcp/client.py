"""
The main client for discovering and loading UTCP tools into LangChain.
"""

from __future__ import annotations

from typing import Any, Dict, List

from langchain_core.tools import BaseTool

# Corrected imports based on the provided file structure
from utcp.data.utcp_client_config import UtcpClientConfigSerializer
from utcp.exceptions.utcp_serializer_validation_error import (
    UtcpSerializerValidationError as UTCPSDKError,
)
from utcp.utcp_client import UtcpClient as OfficialUTCPClient

from .adapter import adapt_utcp_tool
from .exceptions import InitializationError


class UTCPClient:
    """
    A LangChain client that wraps the official python-utcp SDK client.
    """

    _sdk_client: OfficialUTCPClient

    def __init__(self, sdk_client: OfficialUTCPClient):
        """
        Private constructor. Use the `create` factory method instead.
        """
        self._sdk_client = sdk_client

    @classmethod
    async def create(cls, config: Dict[str, Any]) -> UTCPClient:
        """
        Creates and initializes a new UTCPClient instance from a configuration dictionary.

        Args:
            config: A dictionary representing the UTCP client configuration, which
                    will be validated by the SDK's UtcpClientConfigSerializer.
        """
        try:
            validated_config = UtcpClientConfigSerializer().validate_dict(config)
            sdk_client = await OfficialUTCPClient.create(config=validated_config)
            return cls(sdk_client)
        except UTCPSDKError as e:
            raise InitializationError(
                "Failed to initialize the UTCP SDK client."
            ) from e

    async def aload_tools(self) -> List[BaseTool]:
        """
        Fetches all available tools from the configured manuals and adapts them
        into a list of LangChain BaseTool objects.
        """
        # The `search_tools("")` method returns all tools from the repository.
        all_sdk_tools = await self._sdk_client.search_tools("")

        # Adapt each SDK tool into a LangChain tool, passing the client instance
        # so the adapted tool can make calls.
        return [adapt_utcp_tool(tool, self._sdk_client) for tool in all_sdk_tools]
