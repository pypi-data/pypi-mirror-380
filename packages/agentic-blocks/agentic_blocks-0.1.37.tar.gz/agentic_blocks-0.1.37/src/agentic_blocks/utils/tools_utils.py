"""
Utilities for working with tools across different formats.
"""

import json
from typing import Dict, Any, List, get_type_hints
from inspect import signature, getdoc


def langchain_tool_to_openai_format(tool) -> Dict[str, Any]:
    """
    Convert a LangChain StructuredTool to OpenAI function calling format.

    Args:
        tool: A langchain_core.tools.structured.StructuredTool instance

    Returns:
        Dictionary in OpenAI function calling format, compatible with
        MCPClient.list_tools() output and call_llm() tools parameter
    """
    schema = tool.args_schema.model_json_schema()

    # Resolve $ref references by flattening $defs into the schema
    # OpenAI doesn't support $ref/$defs, so we need to inline all definitions
    def resolve_refs(obj, defs):
        if isinstance(obj, dict):
            if "$ref" in obj:
                # Extract the reference path (e.g., "#/$defs/Todo" -> "Todo")
                ref_path = obj["$ref"].split("/")[-1]
                if ref_path in defs:
                    # Return the resolved definition, recursively resolving any nested refs
                    return resolve_refs(defs[ref_path], defs)
                else:
                    return obj  # Keep unresolvable refs as-is
            else:
                # Recursively resolve refs in nested objects
                return {k: resolve_refs(v, defs) for k, v in obj.items()}
        elif isinstance(obj, list):
            # Recursively resolve refs in arrays
            return [resolve_refs(item, defs) for item in obj]
        else:
            return obj

    # Get definitions for reference resolution
    defs = schema.get("$defs", {})

    # Resolve references in properties
    resolved_properties = resolve_refs(schema.get("properties", {}), defs)

    # Build parameters object without $defs
    parameters = {
        "type": "object",
        "properties": resolved_properties,
        "required": schema.get("required", []),
    }

    return {
        "type": "function",
        "function": {
            "name": schema.get("title", tool.name),
            "description": tool.description or schema.get("description", ""),
            "parameters": parameters,
        },
    }


def langchain_tools_to_openai_format(tools: List) -> List[Dict[str, Any]]:
    """
    Convert a list of LangChain StructuredTools to OpenAI function calling format.

    Args:
        tools: List of langchain_core.tools.structured.StructuredTool instances

    Returns:
        List of dictionaries in OpenAI function calling format, compatible with
        MCPClient.list_tools() output and call_llm() tools parameter
    """
    return [langchain_tool_to_openai_format(tool) for tool in tools]


def create_tool_registry(tools: List) -> Dict[str, Any]:
    """
    Create a registry mapping tool names to LangChain tool instances.

    Args:
        tools: List of langchain_core.tools.structured.StructuredTool instances

    Returns:
        Dictionary mapping tool names to tool instances
    """
    return {tool.name: tool for tool in tools}


def execute_tool_call(
    tool_call: Dict[str, Any], tool_registry: Dict[str, Any]
) -> Dict[str, Any]:
    """
    Execute a single tool call using LangChain tool registry.

    Args:
        tool_call: Dictionary with 'tool_name', 'arguments', and 'tool_call_id' keys
        tool_registry: Registry mapping tool names to tool instances

    Returns:
        Dictionary with 'tool_call_id', 'result', and 'is_error' keys
    """
    tool_name = tool_call.get("tool_name")
    arguments = tool_call.get("arguments", {})
    tool_call_id = tool_call.get("tool_call_id")

    try:
        if tool_name not in tool_registry:
            raise ValueError(f"Tool '{tool_name}' not found in registry")

        tool = tool_registry[tool_name]
        result = tool.entrypoint(**arguments)

        return {"tool_call_id": tool_call_id, "result": result, "is_error": False}
    except Exception as e:
        return {
            "tool_call_id": tool_call_id,
            "result": f"Error executing tool '{tool_name}': {str(e)}",
            "is_error": True,
        }


def execute_pending_tool_calls(
    messages, tool_registry: Dict[str, Any]
) -> List[Dict[str, Any]]:
    """
    Execute all pending tool calls from a Messages instance and add responses back.

    Args:
        messages: Messages instance with pending tool calls
        tool_registry: Registry mapping tool names to tool instances

    Returns:
        List of execution results compatible with Messages.add_tool_responses format
    """
    pending_tool_calls = messages.get_pending_tool_calls()
    results = []

    for tool_call in pending_tool_calls:
        result = execute_tool_call(tool_call, tool_registry)

        # Convert to format expected by Messages.add_tool_responses
        if result["is_error"]:
            tool_response = {
                "tool_call_id": result["tool_call_id"],
                "is_error": True,
                "error": result["result"],
            }
        else:
            tool_response = {
                "tool_call_id": result["tool_call_id"],
                "is_error": False,
                "tool_response": result["result"],
            }

        results.append(tool_response)

        # Add tool response back to messages using individual method
        # if result['is_error']:
        #    messages.add_tool_response(result['tool_call_id'], result['result'])
        # else:
        #    messages.add_tool_response(result['tool_call_id'], str(result['result']))

    return results


def execute_and_add_tool_responses(
    messages, tool_registry: Dict[str, Any]
) -> List[Dict[str, Any]]:
    """
    Execute all pending tool calls and add them using Messages.add_tool_responses batch method.

    Args:
        messages: Messages instance with pending tool calls
        tool_registry: Registry mapping tool names to tool instances

    Returns:
        List of execution results compatible with Messages.add_tool_responses format
    """
    pending_tool_calls = messages.get_pending_tool_calls()
    results = []

    for tool_call in pending_tool_calls:
        result = execute_tool_call(tool_call, tool_registry)

        # Convert to format expected by Messages.add_tool_responses
        if result["is_error"]:
            tool_response = {
                "tool_call_id": result["tool_call_id"],
                "is_error": True,
                "error": result["result"],
            }
        else:
            tool_response = {
                "tool_call_id": result["tool_call_id"],
                "is_error": False,
                "tool_response": result["result"],
            }

        results.append(tool_response)

    # Add all responses at once using the batch method
    if results:
        messages.add_tool_responses(results)

    return results


def agno_tool_to_openai_format(tool) -> Dict[str, Any]:
    """
    Convert an agno tool (Function object or @tool decorated function) to OpenAI function calling format.

    Args:
        tool: An agno Function object or @tool decorated function

    Returns:
        Dictionary in OpenAI function calling format, compatible with
        MCPClient.list_tools() output and call_llm() tools parameter
    """
    # Check if this is already an agno Function object
    if (
        hasattr(tool, "name")
        and hasattr(tool, "description")
        and hasattr(tool, "parameters")
    ):
        # This is an agno Function object, ensure parameters are processed
        if hasattr(tool, "process_entrypoint"):
            # Check if parameters are empty (not processed yet)
            default_params = {"type": "object", "properties": {}, "required": []}
            if tool.parameters == default_params:
                tool.process_entrypoint()

        # Clean up parameters to remove (None) from descriptions
        cleaned_parameters = tool.parameters or {
            "type": "object",
            "properties": {},
            "required": [],
        }
        if "properties" in cleaned_parameters:
            for prop_name, prop_data in cleaned_parameters["properties"].items():
                if isinstance(prop_data, dict) and "description" in prop_data:
                    prop_data["description"] = prop_data["description"].replace(
                        "(None) ", ""
                    )

        return {
            "type": "function",
            "function": {
                "name": tool.name,
                "description": (tool.description or "").replace(" (None)", ""),
                "parameters": cleaned_parameters,
            },
        }

    # Otherwise, treat as a raw Python function
    function_name = tool.__name__

    # Get type hints and signature
    sig = signature(tool)
    type_hints = get_type_hints(tool)

    # Build parameters schema
    parameters = {"type": "object", "properties": {}, "required": []}

    for param_name, param in sig.parameters.items():
        if param_name in type_hints:
            # Convert type hint to JSON schema format
            param_type = type_hints[param_name]

            # Basic type conversion
            if param_type is str:
                json_type = "string"
            elif param_type in (int, float):
                json_type = "number"
            elif param_type is bool:
                json_type = "boolean"
            else:
                json_type = "string"  # Default fallback

            parameters["properties"][param_name] = {
                "type": json_type,
                "description": f"Parameter {param_name}",
            }

            # Mark as required if no default value
            if param.default == param.empty:
                parameters["required"].append(param_name)

    return {
        "type": "function",
        "function": {
            "name": function_name,
            "description": getdoc(tool) or "",
            "parameters": parameters,
        },
    }


def agno_tools_to_openai_format(tools: List) -> List[Dict[str, Any]]:
    """
    Convert a list of agno @tool decorated functions to OpenAI function calling format.

    Args:
        tools: List of agno @tool decorated functions

    Returns:
        List of dictionaries in OpenAI function calling format, compatible with
        MCPClient.list_tools() output and call_llm() tools parameter
    """
    return [agno_tool_to_openai_format(tool) for tool in tools]


def print_tool(tool) -> None:
    """
    Print a single LangChain tool in OpenAI format in a readable JSON structure.

    Args:
        tool: A langchain_core.tools.structured.StructuredTool instance
    """
    openai_tool = langchain_tool_to_openai_format(tool)
    print(json.dumps(openai_tool, indent=2))


def print_agno_tool(tool) -> None:
    """
    Print a single agno tool in OpenAI format in a readable JSON structure.

    Args:
        tool: An agno @tool decorated function
    """
    openai_tool = agno_tool_to_openai_format(tool)
    print(json.dumps(openai_tool, indent=2))
