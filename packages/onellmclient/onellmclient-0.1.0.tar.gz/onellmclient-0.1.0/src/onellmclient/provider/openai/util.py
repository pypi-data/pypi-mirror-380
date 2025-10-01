from openai import OpenAI
from typing import Any, Dict, List, Optional, Literal


def client(api_key: str, api_base: str = "https://api.openai.com/v1") -> OpenAI:
    return OpenAI(api_key=api_key, base_url=api_base)


def _reformat_json_schema(schema: Dict[str, Any]) -> Dict[str, Any]:
    """
    给 schema 的 type=object 递归添加 additionalProperties=False
    """
    if schema["type"] == "object":
        schema["additionalProperties"] = False
        for _, value in schema["properties"].items():
            _reformat_json_schema(value)
    return schema


def _reformat_tools(tools: list[Dict[str, Any]]) -> List[Dict[str, Any]]:
    return [
        {
            "type": "function",
            "function": tool,
        }
        for tool in tools
    ]


def convert_unified_payload_to_response_payload(
    model: str,
    messages: List[Dict[str, Any]],
    instructions: Optional[str] = None,
    schema: Optional[Dict[str, Any]] = None,
    tools: Optional[List[Dict[str, Any]]] = None,
    reasoning_effort: Optional[Literal["minimal", "low", "medium", "high"]] = None,
    temperature: Optional[float] = 0.0,
    web_search: Optional[bool] = False,
):
    converted = {
        "model": model,
        "input": messages,
        "instructions": instructions,
        "tools": [],
    }

    if schema is not None:
        converted["text"] = {
            "type": "json_schema",
            "schema": _reformat_json_schema(schema),
            "name": "json_schema",
            "strict": True,
        }

    if tools is not None:
        converted["tools"].extend(_reformat_tools(tools))

    if reasoning_effort is not None and (
        model.startswith("o") or model.startswith("gpt-5")
    ):
        converted["reasoning"] = {"effort": reasoning_effort}

    if temperature is not None:
        converted["temperature"] = temperature

    if web_search:
        converted["tools"].append({"type": "web_search"})

    return converted
