from typing import Any, Dict, List, Optional, Literal
from openai import OpenAI
import warnings, json
from anthropic import Anthropic
from google.genai import Client as Gemini
from .utils import (
    openai_json_schema,
    openai_tools,
    openai_response_convert,
    anthropic_response_convert,
    anthropic_tools,
    gemini_response_convert,
    gemini_messages,
    openai_messages,
    anthropic_messages,
)
from .types import UnifiedToolResultMessageContent,UnifiedMessage,UnifiedToolResult


class Client:
    """统一 LLM 客户端：对齐主要厂商的文本/聊天接口签名。"""

    _openai: Optional[OpenAI]
    _anthropic: Optional[Anthropic]
    _gemini: Optional[Gemini]

    def __init__(
        self,
        openai: Optional[Dict[Literal["key", "base"], str]] = None,
        anthropic: Optional[Dict[Literal["key", "base"], str]] = None,
        gemini: Optional[Dict[Literal["key", "base"], str]] = None,
    ) -> None:
        if openai is not None:
            if openai["key"] is None:
                raise ValueError("OpenAI API key is not set")
            self._openai = OpenAI(api_key=openai["key"], base_url=openai["base"])

        if anthropic is not None:
            if anthropic["key"] is None:
                raise ValueError("Anthropic API key is not set")
            self._anthropic = Anthropic(
                api_key=anthropic["key"], base_url=anthropic["base"]
            )

        if gemini is not None:
            if gemini["key"] is None:
                raise ValueError("Gemini API key is not set")
            self._gemini = Gemini(
                api_key=gemini["key"], http_options={"base_url": gemini["base"]}
            )

    def get_client(self, provider: str) -> Any:
        if provider == "openai":
            return self._openai
        elif provider == "anthropic":
            return self._anthropic
        elif provider == "gemini":
            return self._gemini

        raise ValueError(f"Unsupported provider: {provider}")

    def completion(
        self,
        provider: str,
        model: str,
        messages: List[Dict[str, Any]],
        instructions: Optional[str] = None,
        schema: Optional[Dict[str, Any]] = None,
        tools: Optional[List[Dict[str, Any]]] = None,
        reasoning_effort: Optional[
            Literal["off", "minimal", "low", "medium", "high"]
        ] = None,
        temperature: Optional[float] = None,
        web_search: bool = False,
        tool_choice: Optional[Literal["auto", "none", "required"]] = None,
    ) -> UnifiedMessage:
        """
        统一LLM接口

        Args:
            provider: 提供商
            model: 模型
            messages: 消息
            instructions: 指令
            schema: 模式
            tools: 工具
            reasoning_effort: 推理力度
            temperature: 温度，范围0-2
            web_search: 网络搜索

        Returns:
            UnifiedMessage: 统一响应
        """

        if provider == "openai":
            payload = {
                "model": model,
                "input": openai_messages(messages),
                "stream": False,
                "instructions": instructions,
                "tools": [],
            }
            if schema is not None:
                payload["text"] = {
                    "format": {
                        "type": "json_schema",
                        "schema": openai_json_schema(schema),
                        "name": "json_response",
                        "strict": True,
                    }
                }

            if tools is not None:
                payload["tools"].extend(openai_tools(tools))

            if temperature is not None and not model.startswith("gpt-5"): # gpt-5 not support temperature
                payload["temperature"] = temperature

            if reasoning_effort is not None:
                if reasoning_effort == "off":
                    raise ValueError("reasoning_effort off is not supported")
                payload["reasoning"] = {"effort": reasoning_effort}

            if web_search:
                payload["tools"].append({"type": "web_search"})

            if tool_choice is not None:
                payload["tool_choice"] = tool_choice

            response = self._openai.responses.create(**payload)
            return openai_response_convert(response)

        elif provider == "anthropic":
            payload = {
                "model": model,
                "messages": anthropic_messages(messages),
                "stream": False,
                "max_tokens": 8192 * 2,
                "system": instructions,
                "tools": [],
            }

            if reasoning_effort is not None:
                if reasoning_effort == "off":
                    payload["thinking"] = {"type": "disabled"}
                else:
                    budget_map = {
                        "minimal": int(payload["max_tokens"] * 0.6 * 0.25),
                        "low": int(payload["max_tokens"] * 0.6 * 0.5),
                        "medium": int(payload["max_tokens"] * 0.6 * 0.75),
                        "high": int(payload["max_tokens"] * 0.6 * 1),
                    }
                    payload["thinking"] = {
                        "type": "enabled",
                        "budget_tokens": budget_map[reasoning_effort],
                    }

            if tools is not None:
                payload["tools"].extend(anthropic_tools(tools))

            if schema is not None:
                warnings.warn(
                    "schema is not supported for Anthropic, will be converted to system instruction"
                )
                if payload["system"] is None:
                    payload["system"] = ""
                payload[
                    "system"
                ] += f"\n\nIMPORTANT: YOU MUST RESPOND IN THE JSON SCHEMA FORMAT SPECIFIED BELOW (WITHOUT ANY OTHER TEXT):\n\n{json.dumps(schema)}"

            if temperature is not None:
                payload["temperature"] = round(temperature / 2, 1)

            if web_search:
                payload["tools"].append(
                    {"type": "web_search_20250305", "name": "web_search"}
                )

            if tool_choice is not None:
                tool_choice_map = {
                    "auto": "auto",
                    "none": "none",
                    "required": "any",
                }
                payload["tool_choice"] = {"type": tool_choice_map[tool_choice]}

            response = self._anthropic.messages.create(**payload)
            return anthropic_response_convert(response)

        elif provider == "gemini":
            payload = {
                "model": model,
                "contents": gemini_messages(messages),
                "config": {"tools": []},
            }
            if instructions is not None:
                payload["config"]["system_instruction"] = instructions

            if schema is not None:
                payload["config"]["response_mime_type"] = "application/json"
                payload["config"]["response_schema"] = schema

            if tools is not None:
                payload["config"]["tools"].append({"function_declarations": tools})

            if temperature is not None:
                payload["config"]["temperature"] = temperature

            if web_search:
                payload["config"]["tools"].append({"google_search": {}})

            if tool_choice is not None:
                function_calling_config_map = {
                    "auto": "AUTO",
                    "none": "NONE",
                    "required": "ANY",
                }
                payload["config"]["tool_config"] = {
                    "function_calling_config": {
                        "mode": function_calling_config_map[tool_choice]
                    }
                }

            if reasoning_effort is not None:
                max_budget = 32768 if "pro" in model else 24576
                budget_map = {
                    "off": 0,
                    "minimal": int(max_budget * 0.25),
                    "low": int(max_budget * 0.5),
                    "medium": int(max_budget * 0.75),
                    "high": max_budget,
                }
                payload["config"]["thinking_config"] = {
                    "include_thoughts": False,
                    "thinking_budget": budget_map[reasoning_effort],
                }

            response = self._gemini.models.generate_content(**payload)
            return gemini_response_convert(response)

        raise NotImplementedError(f"Unsupported provider: {provider}")

    def agent(
        self,
        provider: str,
        model: str,
        messages: List[Dict[str, Any]],
        instructions: Optional[str] = None,
        schema: Optional[Dict[str, Any]] = None,
        tools: Optional[List[Dict[str, Any]]] = None,
        reasoning_effort: Optional[
            Literal["off", "minimal", "low", "medium", "high"]
        ] = None,
        temperature: Optional[float] = None,
        web_search: bool = False,
        tool_choice: Optional[Literal["auto", "none", "required"]] = None,
    ) -> UnifiedMessage:
        """
        自动执行 tool call ，返回最后结果
        """
        callable_map = {}
        if tools is not None:
            for tool in tools:
                callable_map[tool["name"]] = tool["handler"]
                del tool["handler"]

        def has_tool_call(message: UnifiedMessage) -> bool:
            if isinstance(message.content, list):
                for content in message.content:
                    if content.type == "tool_call":
                        return True
            return False

        max_tool_call_count = 10
        tool_call_count = 0

        while True:
            response = self.completion(
                provider=provider,
                model=model,
                messages=messages,
                instructions=instructions,
                schema=schema,
                tools=tools,
                reasoning_effort=reasoning_effort,
                temperature=temperature,
                web_search=web_search,
                tool_choice=tool_choice,
            )

            if not has_tool_call(response):
                return response

            tool_call_count += 1
            if tool_call_count >= max_tool_call_count:
                raise Exception(f"Tool call count exceeded max_tool_call_count: {max_tool_call_count}")

            messages.append(response)

            tool_results=[]
            for content in response.content:
                if content.type == "tool_call":
                    try:
                        arguments = content.content.arguments or {}
                        result = {
                            "result": callable_map[content.content.name](**arguments)
                        }
                    except ValueError as e:
                        result = {"error": str(e)}

                    tool_results.append(UnifiedToolResultMessageContent(
                        type='tool_result',
                        content=UnifiedToolResult(
                            content=json.dumps(result),
                            tool_call_id=content.content.id,
                            name=content.content.name
                        )
                    ))

            messages.append(
                UnifiedMessage(
                    role='user',
                    content=tool_results,
                )
            )
