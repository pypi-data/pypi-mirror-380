import json
import re
from typing import Any, Optional, Type

from langchain_core.tools import StructuredTool
from pydantic import BaseModel, create_model

# Corrected imports based on the provided file structure
from utcp.data.tool import Tool as UTCPTool
from utcp.utcp_client import UtcpClient as OfficialUTCPClient

from .exceptions import ToolExecutionError


def _sanitize_tool_name(name: str) -> str:
    """Sanitizes the tool name to be a valid identifier for LangChain."""
    return re.sub(r"[^a-zA-Z0-9_-]", "_", name)


def _create_args_schema(utcp_tool: UTCPTool) -> Type[BaseModel]:
    """Dynamically creates a Pydantic model for the tool's arguments."""
    field_definitions = {}

    # The schema is now under `utcp_tool.inputs`
    if utcp_tool.inputs and utcp_tool.inputs.properties:
        required_fields = utcp_tool.inputs.required or []
        for name, details_dict in utcp_tool.inputs.properties.items():
            # Pydantic v2 create_model expects a tuple of (type, default_value)
            if name in required_fields:
                field_definitions[name] = (Any, ...)  # Required
            else:
                field_definitions[name] = (Optional[Any], None)  # Optional

    sanitized_name = _sanitize_tool_name(utcp_tool.name)
    return create_model(f"{sanitized_name}Args", **field_definitions)


async def _create_tool_coroutine(
    sdk_client: OfficialUTCPClient, tool_name: str, **kwargs: Any
) -> Any:
    """Creates the async function that LangChain will execute."""
    try:
        print(f"Executing tool '{tool_name}' with args: {kwargs}")
        result = await sdk_client.call_tool(tool_name, kwargs)
        # Ensure output is serializable for the agent
        if isinstance(result, (dict, list)):
            return json.dumps(result, indent=2)
        return str(result)
    except Exception as e:
        # Wrap the SDK's exception in our adapter's exception for consistency
        raise ToolExecutionError(f"Execution of tool '{tool_name}' failed.") from e


def adapt_utcp_tool(
    utcp_tool: UTCPTool, sdk_client: OfficialUTCPClient
) -> StructuredTool:
    """
    Adapts a single UTCP tool from the python-utcp SDK into a
    LangChain StructuredTool.
    """
    args_schema = _create_args_schema(utcp_tool)
    sanitized_name = _sanitize_tool_name(utcp_tool.name)

    return StructuredTool.from_function(
        name=sanitized_name,
        description=utcp_tool.description or f"A UTCP tool named {utcp_tool.name}",
        args_schema=args_schema,
        coroutine=lambda **kwargs: _create_tool_coroutine(
            sdk_client, utcp_tool.name, **kwargs
        ),
        func=None,
    )
