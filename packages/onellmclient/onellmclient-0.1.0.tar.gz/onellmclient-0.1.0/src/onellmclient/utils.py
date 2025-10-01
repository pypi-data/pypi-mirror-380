from openai.types.responses.response import Response as OpenAIResponse
from anthropic.types.message import Message as AnthropicMessage
from google.genai.types import GenerateContentResponse as GeminiResponse
from .types import (
    UnifiedMessage,
    UnifiedToolCall,
    UnifiedTextMessageContent,
    UnifiedToolCallMessageContent,
)
import json
from typing import List


def openai_json_schema(schema: dict) -> dict:
    """
    给 schema 的 type=object 递归添加 additionalProperties=False
    """
    if schema["type"] == "object":
        schema["additionalProperties"] = False
        for _, value in schema["properties"].items():
            openai_json_schema(value)
    return schema


def openai_tools(tools: list[dict]) -> list[dict]:
    """
    给 tools 的 type=function 添加 function 字段
    """
    converted = []
    for tool in tools:
        tool["type"] = "function"
        if "parameters" in tool:
            tool["parameters"] = openai_json_schema(tool["parameters"])
        converted.append(tool)
    return converted


def openai_response_convert(response: OpenAIResponse) -> UnifiedMessage:
    """
    将 OpenAI 的 response 转换为统一格式
    """

    role = None
    contents = []

    for output in response.output:
        if output.type == "message":
            role = output.role
            for output_content in output.content:
                if output_content.type == "output_text":
                    contents.append(
                        UnifiedTextMessageContent(
                            type="text", content=output_content.text, id=output.id
                        )
                    )
        elif output.type == "function_call":
            unified_tool_call = UnifiedToolCall(
                id=output.call_id,
                name=output.name,
                arguments=json.loads(output.arguments),
            )
            contents.append(
                UnifiedToolCallMessageContent(
                    type="tool_call", content=unified_tool_call
                )
            )

    return UnifiedMessage(role=role, content=contents)


def openai_messages(messages: List[UnifiedMessage]) -> list:
    """
    将 UnifiedMessage 转换为 OpenAI 的 messages 格式
    """
    converted = []
    for message in messages:
        message_content = message.get("content")
        if isinstance(message_content, list):
            for content in message_content:
                if content.type == "text":
                    _message = {
                        "type": "message",
                        "content": content.get("content"),
                        "role": message.role,
                    }

                    if message.role == "assistant":
                        _message["id"] = content.get("id")

                    converted.append(_message)
                elif content.type == "tool_call":
                    converted.append(
                        {
                            "type": "function_call",
                            # 'id':None,
                            "call_id": content.content.id,
                            "name": content.content.name,
                            "arguments": json.dumps(content.content.arguments),
                        }
                    )
                elif content.type == "tool_result":
                    converted.append(
                        {
                            "type": "function_call_output",
                            "call_id": content.content.tool_call_id,
                            "output": content.content.content,
                        }
                    )
        else:
            converted.append(
                {"role": message.get("role"), "content": message.get("content")}
            )
    return converted


def anthropic_messages(messages: List[UnifiedMessage]) -> list:
    """
    将 UnifiedMessage 转换为 Anthropic 的 messages 格式
    """
    converted = []
    for message in messages:
        message_content = message.get("content")
        if isinstance(message_content, list):
            contents = []
            for content in message_content:
                if content.type == "text":
                    contents.append({"type": "text", "text": content.get("content")})
                elif content.type == "tool_call":
                    contents.append(
                        {
                            "type": "tool_use",
                            "id": content.content.id,
                            "name": content.content.name,
                            "input": content.content.arguments,
                        }
                    )
                elif content.type == "tool_result":
                    contents.append(
                        {
                            "type": "tool_result",
                            "tool_use_id": content.content.tool_call_id,
                            "content": content.content.content,
                        }
                    )
            converted.append({"role": message.get("role"), "content": contents})
        else:
            converted.append({"role": message.get("role"), "content": message.get("content")})
    return converted


def anthropic_response_convert(response: AnthropicMessage) -> UnifiedMessage:
    """
    将 Anthropic 的 response 转换为统一格式
    """
    role = response.role
    contents = []

    for response_content in response.content:

        if response_content.type == "text":
            if response_content.text is not None:
                contents.append(
                    UnifiedTextMessageContent(
                        type="text", content=response_content.text
                    )
                )
        elif response_content.type == "tool_use":
            unified_tool_call = UnifiedToolCall(
                id=response_content.id,
                name=response_content.name,
                arguments=response_content.input,
            )
            contents.append(
                UnifiedToolCallMessageContent(
                    type="tool_call", content=unified_tool_call
                )
            )

    return UnifiedMessage(
        role=role,
        content=contents,
    )


def anthropic_tools(tools: list[dict]) -> list[dict]:
    """
    parameters 字段改为 input_schema 字段
    """
    converted = []
    for tool in tools:
        _converted = {
            "name": tool["name"],
            "description": tool["description"],
        }
        if "parameters" in tool:
            _converted["input_schema"] = tool["parameters"]
        else:
            # Anthropic要求每个工具都必须有input_schema，即使没有参数也要提供空schema
            _converted["input_schema"] = {
                "type": "object",
                "properties": {},
                "required": [],
            }
        converted.append(_converted)
    return converted


def gemini_messages(messages: List[UnifiedMessage]) -> list[dict]:
    """
    将 UnifiedMessage 转换为 Gemini 的 contents 格式
    """
    converted = []
    for message in messages:
        # 处理角色映射：assistant -> model, 其他保持不变

        role = "model" if message.get("role") == "assistant" else message.get("role")

        if isinstance(message.get("content"), list):
            parts = []
            for content in message.get("content"):
                if content.type == "text":
                    parts.append({"text": content.get("content")})
                elif content.type == "tool_call":
                    parts.append(
                        {
                            "function_call": {
                                "name": content.get("content").get("name"),
                                "args": content.get("content").get("arguments") or {},
                            }
                        }
                    )
                elif content.type == "tool_result":
                    parts.append(
                        {
                            "function_response": {
                                "name": content.content.name,
                                "response": json.loads(content.content.content),
                            }
                        }
                    )
            converted.append({"role": role, "parts": parts})
        else:
            # 纯字符串内容
            converted.append(
                {"role": role, "parts": [{"text": message.get("content")}]}
            )

    return converted


def gemini_tools(tools: list[dict]) -> list[dict]:
    """
    将统一工具格式转换为 Gemini 的 functionDeclarations 格式
    """
    function_declarations = []
    for tool in tools:
        function_declaration = {
            "name": tool["name"],
            "description": tool["description"],
        }
        if "parameters" in tool:
            function_declaration["parameters"] = tool["parameters"]
        else:
            # Gemini 如果没有参数，可以省略 parameters 字段
            pass
        function_declarations.append(function_declaration)

    return [{"function_declarations": function_declarations}]


def gemini_response_convert(response: GeminiResponse) -> UnifiedMessage:
    """
    将 Gemini 的 response 转换为统一格式
    """

    role = response.candidates[0].content.role

    if role != "model":
        raise ValueError(f"Gemini response role is not model: {role}")

    role = "assistant"
    contents = []

    for part in response.candidates[0].content.parts:
        if hasattr(part, "text") and part.text is not None:
            contents.append(UnifiedTextMessageContent(type="text", content=part.text))

        if hasattr(part, "function_call") and part.function_call is not None:
            unified_tool_call = UnifiedToolCall(
                id=part.function_call.id if hasattr(part.function_call, "id") else None,
                name=(
                    part.function_call.name
                    if hasattr(part.function_call, "name")
                    else None
                ),
                arguments=(
                    part.function_call.args
                    if hasattr(part.function_call, "args")
                    else None
                ),
            )
            contents.append(
                UnifiedToolCallMessageContent(
                    type="tool_call", content=unified_tool_call
                )
            )

        # 处理 function_response（虽然模型通常不会返回这个，但为了完整性）
        if hasattr(part, "function_response") and part.function_response is not None:
            from .types import UnifiedToolResult, UnifiedToolResultMessageContent

            unified_tool_result = UnifiedToolResult(
                type="tool_result",
                content=str(part.function_response.response),
                tool_call_id=part.function_response.name,  # 使用函数名作为标识
            )
            contents.append(
                UnifiedToolResultMessageContent(
                    type="tool_result", content=unified_tool_result
                )
            )

    return UnifiedMessage(
        role=role,
        content=contents,
    )
