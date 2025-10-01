# onellmclient

统一主要 LLM 提供商（OpenAI、Anthropic、Gemini）接口格式的 Python 客户端。

- 运行时零强制依赖；通过 extras 按需安装各家 SDK。
- 提供统一的 `Client` 接口以便上层应用透明切换供应商。

## 安装

使用 uv（推荐）：

```bash
uv venv
uv pip install -e .
# 或安装某家 SDK：
uv pip install -e .[openai]
uv pip install -e .[anthropic]
uv pip install -e .[gemini]
uv pip install -e .[all]
```

## 构建与发布

使用 uv 构建 sdist 与 wheel：

```bash
uv build
ls dist/
```

发布到 TestPyPI：

```bash
uv tool install twine  # 首次需要安装
uv run twine upload --repository testpypi dist/*
# 安装测试：
uv pip install -i https://test.pypi.org/simple/ onellmclient==0.1.0
```

发布到 PyPI（确认版本号已递增且能在 TestPyPI 正常安装后）：

```bash
uv run twine upload dist/*
```

## 使用

```python
from onellmclient import Client

client = Client(openai={"api_key": "..."})
resp = client.completion(
    provider="openai", model="gpt-4o-mini", messages=[{"role":"user","content":"hi"}]
)
print(resp)
```

## 开源协议

MIT
