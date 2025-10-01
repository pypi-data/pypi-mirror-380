"""Utilities for formatting chat messages into prompt strings.

This module provides helper functions for working with chat messages in the format used by
OpenAI's chat models.
"""

from __future__ import annotations

import importlib.util
import json
import warnings
from concurrent.futures import ThreadPoolExecutor
from copy import deepcopy
from typing import TYPE_CHECKING, Any, Literal, Optional, Union, cast

from requests import get

if TYPE_CHECKING:
    from openai.types.chat import ChatCompletion, ChatCompletionMessage, ChatCompletionMessageParam
    from openai.types.responses import Response


# Define message prefixes
_SYSTEM_PREFIX = "System: "
_USER_PREFIX = "User: "
_ASSISTANT_PREFIX = "Assistant: "
_TOOL_PREFIX = "Tool: "

# Define role constants
_SYSTEM_ROLE: Literal["system"] = "system"
_DEVELOPER_ROLE: Literal["developer"] = "developer"
_USER_ROLE: Literal["user"] = "user"
_TOOL_ROLE: Literal["tool"] = "tool"
_ASSISTANT_ROLE: Literal["assistant"] = "assistant"


# Define system roles
_SYSTEM_ROLES = [_SYSTEM_ROLE, _DEVELOPER_ROLE]

# Define message type constants
_FUNCTION_CALL_TYPE = "function_call"
_FUNCTION_CALL_OUTPUT_TYPE = "function_call_output"

# Define XML tag constants
_TOOLS_TAG_START = "<tools>"
_TOOLS_TAG_END = "</tools>"
_TOOL_CALL_TAG_START = "<tool_call>"
_TOOL_CALL_TAG_END = "</tool_call>"
_TOOL_RESPONSE_TAG_START = "<tool_response>"
_TOOL_RESPONSE_TAG_END = "</tool_response>"

# Define Unique OpenAI Tool IDs

_WEB_SEARCH_CALL = "web_search_call"
_FILE_SEARCH_CALL = "file_search_call"

# Define tool-related message prefixes
_TOOL_DEFINITIONS_PREFIX = (
    "You are an AI Assistant that can call provided tools (a.k.a. functions). "
    "The set of available tools is provided to you as function signatures within "
    f"{_TOOLS_TAG_START} {_TOOLS_TAG_END} XML tags. "
    "You may call one or more of these functions to assist with the user query. If the provided functions are not helpful/relevant, "
    "then just respond in natural conversational language. "
    "After you choose to call a function, you will be provided with the function's results within "
    f"{_TOOL_RESPONSE_TAG_START} {_TOOL_RESPONSE_TAG_END} XML tags.\n\n"
    f"{_TOOLS_TAG_START}\n"
)

_TOOL_CALL_SCHEMA_PREFIX = (
    "For each function call return a JSON object, with the following pydantic model json schema:\n"
    "{'name': <function-name>, 'arguments': <args-dict>}\n"
    f"Each function call should be enclosed within {_TOOL_CALL_TAG_START} {_TOOL_CALL_TAG_END} XML tags.\n"
    "Example:\n"
    f"{_TOOL_CALL_TAG_START}\n"
    "{'name': <function-name>, 'arguments': <args-dict>}\n"
    f"{_TOOL_CALL_TAG_END}\n"
    "Note: Function calls and their results may optionally include a call_id, which should be ignored."
)

# Set up a URL cache so that we can avoid fetching the same URL multiple times
_url_cache: dict[str, str] = {}


# Responses and Chat Completions


def _format_tools_prompt(tools: list[dict[str, Any]], is_responses: bool = False) -> str:
    """
    Format a list of tool definitions into a system message with tools.

    Args:
        tools (List[Dict[str, Any]]): The list of tools made available for the LLM to use when responding to the messages.
            This is the same argument as the tools argument for OpenAI's Responses API or Chat Completions API.
            This list of tool definitions will be formatted into a system message.
        is_responses (bool): Whether the tools are in Responses API format.

    Returns:
        str: Formatted string with tools as a system message.
    """
    system_message = _TOOL_DEFINITIONS_PREFIX

    # Format each tool as a function spec
    tool_strings = []
    for tool in tools:
        if not is_responses:
            tool_dict = {
                "type": "function",
                "function": {
                    "name": tool["function"]["name"],
                    "description": tool["function"]["description"],
                    "parameters": tool["function"]["parameters"],
                },
            }
        # responses format
        elif tool["type"] == "function":
            tool_dict = {
                "type": "function",
                "name": tool["name"],
                "description": tool["description"],
                "parameters": tool["parameters"],
                "strict": tool.get("strict", True),
            }
        elif tool["type"] == "file_search":
            tool_dict = {
                "type": "function",
                "name": "file_search",
                "description": "Search user-uploaded documents for relevant passages.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "queries": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Search queries to run against the document index.",
                        },
                    },
                    "required": ["queries"],
                },
            }
        elif tool["type"] == "web_search":
            if importlib.util.find_spec("trafilatura"):
                tool_dict = {
                    "type": "function",
                    "name": _WEB_SEARCH_CALL,
                    "description": "Search the web for relevant information.",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "query": {
                                "type": "string",
                                "description": "Search the web with a query and return relevant pages.",
                            },
                        },
                        "required": ["query"],
                    },
                }
            else:
                warnings.warn(
                    "You must install trafilatura in order to properly score web search requests.",
                    UserWarning,
                    stacklevel=2,
                )
                continue
        else:
            continue
        tool_strings.append(json.dumps(tool_dict, separators=(",", ":")))

    system_message += "\n".join(tool_strings)
    system_message += f"\n{_TOOLS_TAG_END}\n\n"
    system_message += _TOOL_CALL_SCHEMA_PREFIX

    return system_message


def _get_prefix(msg: dict[str, Any], prev_msg_role: Optional[str] = None) -> str:
    """
    Get the appropriate prefix for a message based on its role.

    Args:
        msg (Dict[str, Any]): A message dictionary containing at least a 'role' key.
        prev_msg_role (Optional[str]): The role of the previous message, if any.

    Returns:
        str: The appropriate prefix for the message role.
    """
    role = str(msg.get("name", msg["role"]))

    # Skip prefix for system messages if the previous message was also a system message
    if role in _SYSTEM_ROLES and prev_msg_role in _SYSTEM_ROLES:
        return ""

    if role in _SYSTEM_ROLES:
        return _SYSTEM_PREFIX
    if role == _USER_ROLE:
        return _USER_PREFIX
    if role == _ASSISTANT_ROLE:
        return _ASSISTANT_PREFIX
    return role.capitalize() + ": "


def _find_index_after_first_system_block(messages: list[dict[str, Any]]) -> int:
    """
    Find the index after the first consecutive block of system messages.

    Args:
        messages (List[Dict]): A list of message dictionaries.

    Returns:
        int: The index after the first consecutive block of system messages.
             Returns -1 if no system messages are found.
    """
    last_system_idx = -1
    for i, msg in enumerate(messages):
        if msg.get("role") in _SYSTEM_ROLES:
            last_system_idx = i
        else:
            # Found a non-system message, so we've reached the end of the first system block
            break

    return last_system_idx


def form_prompt_string(
    messages: list[dict[str, Any]],
    tools: Optional[list[dict[str, Any]]] = None,
    use_responses: Optional[bool] = None,
    **responses_api_kwargs: Any,
) -> str:
    """
    Convert a list of chat messages into a single string prompt.

    If there is only one message and no tools are provided, returns the content directly.
    Otherwise, concatenates all messages with appropriate role prefixes and ends with
    "Assistant:" to indicate the assistant's turn is next.

    If tools are provided, they will be formatted as a system message at the start
    of the prompt. In this case, even a single message will use role prefixes since
    there will be at least one system message (the tools section).

    If Responses API kwargs (like instructions) are provided, they will be
    formatted for the Responses API format. These kwargs are only supported
    for the Responses API format.

    Handles messages in either OpenAI's [Responses API](https://platform.openai.com/docs/api-reference/responses) or [Chat Completions API](https://platform.openai.com/docs/api-reference/chat) formats.

    Args:
        messages (List[Dict]): A list of dictionaries representing chat messages.
            Each dictionary should contain either:
            For Responses API:
            - 'role' and 'content' for regular messages
            - 'type': 'function_call' and function call details for tool calls
            - 'type': 'function_call_output' and output details for tool results
            For chat completions API:
            - 'role': 'user', 'assistant', 'system', or 'tool' and appropriate content
            - For assistant messages with tool calls: 'tool_calls' containing function calls
            - For tool messages: 'tool_call_id' and 'content' for tool responses
        tools (Optional[List[Dict[str, Any]]]): The list of tools made available for the LLM to use when responding to the messages.
            This is the same argument as the tools argument for OpenAI's Responses API or Chat Completions API.
            This list of tool definitions will be formatted into a system message.
        use_responses (Optional[bool]): If provided, explicitly specifies whether to use Responses API format.
            If None, the format is automatically detected using _uses_responses_api.
            Cannot be set to False when Responses API kwargs are provided.
        **responses_api_kwargs: Optional keyword arguments for OpenAI's Responses API. Currently supported:
            - instructions (str): Developer instructions to prepend to the prompt with highest priority.

    Returns:
        str: A formatted string representing the chat history as a single prompt.

    Raises:
        ValueError: If Responses API kwargs are provided with use_responses=False.
    """
    is_responses = _uses_responses_api(messages, tools, use_responses, **responses_api_kwargs)

    return (
        _form_prompt_responses_api(messages, tools, **responses_api_kwargs)
        if is_responses
        else _form_prompt_chat_completions_api(cast(list["ChatCompletionMessageParam"], messages), tools)
    )


def _get_role(message: dict[str, Any]) -> str:
    if message.get("type", "message") == "message":
        return cast(str, message.get("role", _USER_ROLE))
    if message["type"] == _FUNCTION_CALL_TYPE:
        return _ASSISTANT_ROLE
    if message["type"] == _FUNCTION_CALL_OUTPUT_TYPE:
        return _TOOL_ROLE
    if message["type"] == _FILE_SEARCH_CALL:
        return _TOOL_ROLE
    if message["type"] == _WEB_SEARCH_CALL:
        return _TOOL_ROLE
    return _USER_ROLE


# Chat Completions


def _form_prompt_chat_completions_api(
    messages: list[ChatCompletionMessageParam],
    tools: Optional[list[dict[str, Any]]] = None,
) -> str:
    """
    Convert messages in [OpenAI Chat Completions API format](https://platform.openai.com/docs/api-reference/chat) into a single prompt string.

    Args:
        messages (List[ChatCompletionsMessageParam]): A list of dictionaries representing chat messages in chat completions API format.
        tools (Optional[List[Dict[str, Any]]]): The list of tools made available for the LLM to use when responding to the messages.
        This is the same argument as the tools argument for OpenAI's Chat Completions API.
        This list of tool definitions will be formatted into a system message.

    Returns:
        str: A formatted string representing the chat history as a single prompt.
    """
    messages = messages.copy()
    output = ""

    # Find the index after the first consecutive block of system messages
    last_system_idx = _find_index_after_first_system_block(cast(list[dict[str, Any]], messages))

    if tools is not None and len(tools) > 0:
        messages.insert(
            last_system_idx + 1,
            {
                "role": "system",
                "content": _format_tools_prompt(tools, is_responses=False),
            },
        )

    # Only return content directly if there's a single user message AND no tools
    if len(messages) == 1 and messages[0].get("role") == _USER_ROLE and (tools is None or len(tools) == 0):
        first_msg = cast(dict[str, Any], messages[0])
        return output + str(first_msg["content"])

    # Warn if the last message is an assistant message with tool calls
    if messages and (messages[-1].get("role") == _ASSISTANT_ROLE or "tool_calls" in messages[-1]):
        warnings.warn(
            "The last message is a tool call or assistant message. The next message should not be an LLM response. "
            "This prompt should not be used for trustworthiness scoring.",
            UserWarning,
            stacklevel=2,
        )

    # Track function names by call_id for function call outputs
    function_names = {}
    prev_msg_role = None

    for msg in messages:
        if msg["role"] == _ASSISTANT_ROLE:
            output += _ASSISTANT_PREFIX
            # Handle content if present
            content_value = cast(Optional[str], msg.get("content"))
            if content_value:
                output += f"{content_value}\n\n"
            # Handle tool calls if present
            if "tool_calls" in msg:
                for tool_call in msg["tool_calls"]:
                    if tool_call["type"] == "function":
                        call_id = tool_call["id"]
                        function_names[call_id] = tool_call["function"]["name"]
                        # Format function call as JSON within XML tags, now including call_id
                        function_call = {
                            "name": tool_call["function"]["name"],
                            "arguments": json.loads(tool_call["function"]["arguments"])
                            if tool_call["function"]["arguments"]
                            else {},
                            "call_id": call_id,
                        }
                        output += (
                            f"{_TOOL_CALL_TAG_START}\n{json.dumps(function_call, indent=2)}\n{_TOOL_CALL_TAG_END}\n\n"
                        )
        elif msg["role"] == _TOOL_ROLE:
            # Handle tool responses
            output += _TOOL_PREFIX
            call_id = msg["tool_call_id"]
            name = function_names.get(call_id, "function")
            # Format function response as JSON within XML tags
            tool_response = {"name": name, "call_id": call_id, "output": msg["content"]}
            output += f"{_TOOL_RESPONSE_TAG_START}\n{json.dumps(tool_response, indent=2)}\n{_TOOL_RESPONSE_TAG_END}\n\n"
        else:
            prefix = _get_prefix(cast(dict[str, Any], msg), prev_msg_role)
            output += f"{prefix}{msg['content']}\n\n"
            prev_msg_role = msg["role"]

    output += _ASSISTANT_PREFIX
    return output.strip()


def form_response_string_chat_completions(response: ChatCompletion) -> str:
    """Form a single string representing the response, out of the raw response object returned by OpenAI's Chat Completions API.

    This function extracts the assistant's response message from a ChatCompletion object
    and formats it into a single string representation using the Chat Completions API format.
    It handles both text content and tool calls, formatting them consistently with the
    format used in other functions in this module.

    Args:
        response (ChatCompletion): A ChatCompletion object returned by OpenAI's
            chat.completions.create(). The function uses the first choice
            from the response (response.choices[0].message).

    Returns:
        str: A formatted string containing the response content and any tool calls.
             Tool calls are formatted as XML tags containing JSON with function
             name and arguments, consistent with the format used in form_prompt_string.

    See also:
        [form_response_string_chat_completions_api](#function-form_response_string_chat_completions_api)
    """
    response_msg = response.choices[0].message
    return form_response_string_chat_completions_api(response_msg)


def form_response_string_chat_completions_api(
    response: Union[dict[str, Any], ChatCompletionMessage],
) -> str:
    """
    Form a single string representing the response, out of an assistant response message dictionary in Chat Completions API format.

    Given a ChatCompletion object `response` from OpenAI's `chat.completions.create()`,
    this function can take either a ChatCompletionMessage object from `response.choices[0].message`
    or a dictionary from `response.choices[0].message.to_dict()`.

    All inputs are formatted into a string that includes both content and tool calls (if present).
    Tool calls are formatted using XML tags with JSON content, consistent with the format
    used in `form_prompt_string`.

    Args:
        response (Union[dict[str, Any], ChatCompletionMessage]): Either:
            - A ChatCompletionMessage object from the OpenAI response
            - A chat completion response message dictionary, containing:
              - 'content' (str): The main response content from the LLM
              - 'tool_calls' (List[Dict], optional): List of tool calls made by the LLM,
                where each tool call contains function name and arguments

    Returns:
        str: A formatted string containing the response content and any tool calls.
             Tool calls are formatted as XML tags containing JSON with function
             name and arguments.

    Raises:
        TypeError: If response is not a dictionary or ChatCompletionMessage object.
    """
    response_dict = _chat_completion_message_to_dict(response)
    content = response_dict.get("content") or ""
    tool_calls = cast(Optional[list[dict[str, Any]]], response_dict.get("tool_calls"))
    if tool_calls is not None:
        try:
            rendered_calls: list[str] = []
            for call in tool_calls:
                function_dict = call["function"]
                name = cast(str, function_dict["name"])
                args_str = cast(Optional[str], function_dict.get("arguments"))
                args_obj = json.loads(args_str) if args_str else {}
                rendered_calls.append(
                    f"{_TOOL_CALL_TAG_START}\n{json.dumps({'name': name, 'arguments': args_obj}, indent=2)}\n{_TOOL_CALL_TAG_END}"
                )
            tool_calls_str = "\n".join(rendered_calls)
            return f"{content}\n{tool_calls_str}".strip() if content else tool_calls_str
        except (KeyError, TypeError, json.JSONDecodeError) as e:
            # Log the error but continue with just the content
            warnings.warn(
                f"Error formatting tool_calls in response: {e}. Returning content only.",
                UserWarning,
                stacklevel=2,
            )

    return str(content)


def _chat_completion_message_to_dict(response: Any) -> dict[str, Any]:
    # `response` should be a Union[dict[str, Any], ChatCompletionMessage], but last isinstance check wouldn't be reachable
    if isinstance(response, dict):
        # Start with this isinstance check first to import `openai` lazily
        return response

    try:
        from openai.types.chat import ChatCompletionMessage
    except ImportError as e:
        raise ImportError(
            "OpenAI is required to handle ChatCompletionMessage objects directly. Please install it with `pip install openai`."
        ) from e

    if not isinstance(response, ChatCompletionMessage):
        raise TypeError(
            f"Expected response to be a dict or ChatCompletionMessage object, got {type(response).__name__}"
        )

    return response.model_dump()


# Responses


def _uses_responses_api(
    messages: list[dict[str, Any]],
    tools: Optional[list[dict[str, Any]]] = None,
    use_responses: Optional[bool] = None,
    **responses_api_kwargs: Any,
) -> bool:
    """
    Determine if the messages and parameters indicate Responses API format.

    Args:
        messages (List[Dict]): A list of dictionaries representing chat messages.
        tools (Optional[List[Dict[str, Any]]]): The list of tools made available for the LLM.
        use_responses (Optional[bool]): If provided, explicitly specifies whether to use Responses API format.
            Cannot be set to False when Responses API kwargs are provided.
        **responses_api_kwargs: Optional keyword arguments for OpenAI's Responses API. Currently supported:
            - instructions (str): Developer instructions to prepend to the prompt with highest priority.

    Returns:
        bool: True if using Responses API format, False if using chat completions API format.

    Raises:
        ValueError: If Responses API kwargs are provided with use_responses=False.
    """
    # First check if explicitly set to False while having Responses API kwargs
    if use_responses is False and responses_api_kwargs:
        raise ValueError(
            "Responses API kwargs are only supported in Responses API format. Cannot use with use_responses=False."
        )

    # If explicitly set to True or False, respect that (after validation above)
    if use_responses is not None:
        return use_responses

    # Check for Responses API kwargs
    responses_api_keywords = {"instructions", "input"}
    if any(key in responses_api_kwargs for key in responses_api_keywords):
        return True

    # Check messages for Responses API format indicators
    if any(msg.get("type") in [_FUNCTION_CALL_TYPE, _FUNCTION_CALL_OUTPUT_TYPE] for msg in messages):
        return True

    # Check tools for Responses API format indicators
    if tools and any("name" in tool and "function" not in tool for tool in tools):
        return True

    return False


def _form_prompt_responses_api(
    messages: list[dict[str, Any]] | str,
    tools: Optional[list[dict[str, Any]]] = None,
    response: Optional[Response] = None,
    **responses_api_kwargs: Any,
) -> str:
    """
    Convert messages in [OpenAI Responses API format](https://platform.openai.com/docs/api-reference/responses) into a single prompt string.

    Args:
        messages (List[Dict]): A list of dictionaries representing chat messages in Responses API format.
        tools (Optional[List[Dict[str, Any]]]): The list of tools made available for the LLM to use when responding to the messages.
            This is the same argument as the tools argument for OpenAI's Responses API.
            This list of tool definitions will be formatted into a system message.
        response (Optional[Response]): If provided, then any tool-use outputs in this OpenAI Response object are also added into the prompt string given to TLM.
            Specifically, all items in `response.output` before the final assistant message in `response` are added into the prompt string.
            This includes any tool calls for either user-defined or OpenAI built-in Tools.
             Special-case: If OpenAI's built-in `web_search` tool was used for this response,
             then the returned prompt string will contain text fetched from webpages whose URLs were cited by the following assistant message.
             If there are no tool calls in the `response`, then nothing extra is added to the returned prompt string.
        **responses_api_kwargs: Optional keyword arguments for OpenAI's Responses API. Currently supported:
            - instructions (str): Developer instructions to prepend to the prompt with highest priority.

    Returns:
        str: A formatted string representing the chat history as a single prompt.
    """

    messages = [{"role": "user", "content": messages}] if isinstance(messages, str) else deepcopy(messages)

    if response:
        for i, message in enumerate(response.output[:-1]):
            raw_message = message.model_dump()
            if message.type == _WEB_SEARCH_CALL:
                next_text_message = response.output[i + 1]
                if next_text_message.type != "message":
                    continue
                next_text_content = next_text_message.content[0]
                if next_text_content.type != "output_text":
                    continue
                raw_message["annotations"] = [annotation.model_dump() for annotation in next_text_content.annotations]
            messages.append(raw_message)

    output = ""

    # Find the index after the first consecutive block of system messages
    last_system_idx = _find_index_after_first_system_block(messages)

    # Insert tool definitions and instructions after system messages if needed
    if tools is not None and len(tools) > 0:
        messages.insert(
            last_system_idx + 1,
            {
                "role": _SYSTEM_ROLE,
                "content": _format_tools_prompt(tools, is_responses=True),
            },
        )

    if "instructions" in responses_api_kwargs:
        messages.insert(0, {"role": _SYSTEM_ROLE, "content": responses_api_kwargs["instructions"]})

    # Only return content directly if there's a single user message AND no prepended content
    if len(messages) == 1 and messages[0].get("role") == _USER_ROLE and not output:
        return str(messages[0]["content"])

    # Warn if the last message is a tool call
    if messages and messages[-1].get("type") == _FUNCTION_CALL_TYPE:
        warnings.warn(
            "The last message is a tool call or assistant message. The next message should not be an LLM response. "
            "This prompt should not be used for trustworthiness scoring.",
            UserWarning,
            stacklevel=2,
        )

    return (_responses_messages_to_string(messages) + "\n\n" + _ASSISTANT_PREFIX).strip()


def form_response_string_responses_api(response: Response) -> str:
    """
    Format an assistant response message dictionary from the Responses API into a single string.

    Given a Response object from the Responses API, this function formats the response into a string
    that includes both content and tool calls (if present). Tool calls are formatted using XML tags
    with JSON content, consistent with the format used in `form_prompt_string`.

    Args:
        response (Responses): A Response object from the OpenAI Responses API containing output elements with message content and/or function calls

    Returns:
        str: A formatted string containing the response content and any tool calls.
             Tool calls are formatted as XML tags containing JSON with function
             name and arguments.

    Raises:
        ImportError: If openai is not installed.
    """

    return _responses_messages_to_string([response.output[-1].model_dump()]).replace("Assistant:", "", 1).strip()


def _responses_messages_to_string(messages: list[dict[str, Any]]) -> str:
    content_parts = []

    adjusted_messages = []
    for message in messages:
        if message.get("type", "message") != "message" and message.get("content"):
            adjusted_messages.append({"role": _ASSISTANT_ROLE, "content": message["content"]})

        adjusted_messages.append(message)

    for i, message in enumerate(adjusted_messages):
        if message.get("type", "message") == "message":
            if isinstance(message["content"], str):
                output_content = message["content"]
            else:
                output_content = "\n".join(
                    [content["text"] for content in message["content"] if content["type"] == "output_text"]
                )

            if i == 0 or _get_role(message) != _get_role(adjusted_messages[i - 1]):
                content_parts.append(_get_prefix(message, adjusted_messages[i - 1].get("role") if i > 0 else None))
            content_parts.append(output_content)

        elif message["type"] == "reasoning":
            continue

        elif message["type"] == _FUNCTION_CALL_TYPE:
            try:
                arguments = json.loads(message["arguments"]) if message["arguments"] else {}
                tool_call = {
                    "name": message["name"],
                    "arguments": arguments,
                    "call_id": message["call_id"],
                }

                if i == 0 or _get_role(adjusted_messages[i - 1]) != _ASSISTANT_ROLE:
                    content_parts.append(_ASSISTANT_PREFIX)
                content_parts.append(f"{_TOOL_CALL_TAG_START}\n{json.dumps(tool_call, indent=2)}\n{_TOOL_CALL_TAG_END}")
            except (AttributeError, TypeError, json.JSONDecodeError) as e:
                warnings.warn(
                    f"Error formatting tool call in response: {e}. Skipping this tool call.",
                    UserWarning,
                    stacklevel=2,
                )

        elif message["type"] == _FUNCTION_CALL_OUTPUT_TYPE:
            try:
                tool_call = next(m for m in adjusted_messages[:i] if m.get("call_id", "") == message["call_id"])

                tool_response = {
                    "name": tool_call["name"],
                    "call_id": message["call_id"],
                    "output": message["output"],
                }
                response = json.dumps(tool_response, indent=2)

                if i == 0 or _get_role(adjusted_messages[i - 1]) != _TOOL_ROLE:
                    content_parts.append(_TOOL_PREFIX)
                content_parts.append(f"{_TOOL_RESPONSE_TAG_START}\n{response}\n{_TOOL_RESPONSE_TAG_END}")
            except (AttributeError, TypeError, json.JSONDecodeError) as e:
                warnings.warn(
                    f"Error formatting tool call response: {e}. Skipping this tool call.",
                    UserWarning,
                    stacklevel=2,
                )

        elif message["type"] == _FILE_SEARCH_CALL:
            if message["results"] is None:
                warnings.warn(
                    "File search call returned no results. Please include include=['file_search_call.results'] in your request.",
                    UserWarning,
                    stacklevel=2,
                )
                continue

            tool_call = {
                "name": "file_search",
                "arguments": {"queries": message["queries"]},
                "call_id": message["id"],
            }

            if i == 0 or _get_role(adjusted_messages[i - 1]) != _ASSISTANT_ROLE:
                content_parts.append(_ASSISTANT_PREFIX)
            content_parts.append(f"{_TOOL_CALL_TAG_START}\n{json.dumps(tool_call, indent=2)}\n{_TOOL_CALL_TAG_END}\n\n")

            results_list = [
                {
                    "attributes": result["attributes"],
                    "file_id": result["file_id"],
                    "filename": result["filename"],
                    "score": result["score"],
                    "text": result["text"],
                }
                for result in message["results"]
            ]

            tool_call_response = {
                "name": "file_search",
                "call_id": message["id"],
                "output": results_list,
            }

            content_parts.append(_TOOL_PREFIX)
            content_parts.append(
                f"{_TOOL_RESPONSE_TAG_START}\n{json.dumps(tool_call_response, indent=2)}\n{_TOOL_RESPONSE_TAG_END}"
            )

        elif message["type"] == _WEB_SEARCH_CALL:
            try:
                from trafilatura import extract
            except Exception:
                raise ImportError(
                    "The trafilatura package is required to score responses involving web search. Please install it: `pip install trafilatura`"
                )

            if message["action"]["type"] == "search":
                if "annotations" in message:
                    annotations = message["annotations"]
                else:
                    next_text_message = adjusted_messages[i + 1]
                    if next_text_message["type"] != "message":
                        continue
                    next_text_content = next_text_message["content"][0]
                    if next_text_content["type"] != "output_text":
                        continue
                    annotations = next_text_content["annotations"]

                urls = list(
                    {
                        (annotation["url"], annotation["title"])
                        for annotation in annotations
                        if annotation["type"] == "url_citation"
                    }
                )

                with ThreadPoolExecutor() as executor:

                    def extract_text(pair: tuple[str, str]) -> str:
                        fallback_text = "Response is not shown, but the LLM can still access it. Assume that whatever the LLM references in this URL is true."

                        try:
                            url = pair[0]
                            if url in _url_cache:
                                return _url_cache[url]

                            response_text = extract(
                                get(
                                    url,
                                    timeout=5,
                                    headers={"User-Agent": "Mozilla/5.0"},
                                ).text,
                                output_format="markdown",
                                favor_recall=True,
                            )
                        except Exception:
                            return fallback_text
                        else:
                            if response_text is None:
                                return fallback_text

                            response = response_text.encode("ascii", "ignore").decode("ascii")[:50_000]
                            _url_cache[url] = response

                            return response

                    requests = list(
                        executor.map(
                            extract_text,
                            urls,
                        )
                    )

                websites = [
                    {
                        "url": url,
                        "title": title,
                        "content": data,
                    }
                    for (url, title), data in zip(urls, requests)
                ]

                tool_call = {
                    "name": _WEB_SEARCH_CALL,
                    "arguments": {"query": message["action"]["query"]},
                    "call_id": message["id"],
                }

                tool_response = {
                    "name": _WEB_SEARCH_CALL,
                    "call_id": message["id"],
                    "output": websites,
                }

                if i == 0 or _get_role(adjusted_messages[i - 1]) != _ASSISTANT_ROLE:
                    content_parts.append(_ASSISTANT_PREFIX)
                content_parts.append(
                    f"{_TOOL_CALL_TAG_START}\n{json.dumps(tool_call, indent=2)}\n{_TOOL_CALL_TAG_END}\n\n"
                )

                content_parts.append(_TOOL_PREFIX)
                content_parts.append(
                    f"{_TOOL_RESPONSE_TAG_START}\n{json.dumps(tool_response, indent=2)}\n{_TOOL_RESPONSE_TAG_END}"
                )

            else:
                warnings.warn(
                    f"Unexpected output type: {message['type']} - {message['action']['type']}. Skipping this output.",
                    UserWarning,
                    stacklevel=2,
                )

        else:
            warnings.warn(
                f"Unexpected output type: {message['type']}. Skipping this output.",
                UserWarning,
                stacklevel=2,
            )

        content_parts.append("\n\n")

    return "".join(content_parts).strip()
