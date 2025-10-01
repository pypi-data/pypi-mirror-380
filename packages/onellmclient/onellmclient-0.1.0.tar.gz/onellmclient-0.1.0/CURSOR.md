# CURSOR.md

统一LLM接口客户端

## 技术架构
- 语言：Python 3.9+
- 构建：hatchling（PEP 517/518）
- 环境管理：uv（推荐）
- 包布局：`src/` 结构

## 项目结构
- `src/onellmclient/`：核心包
- `tests/`：单元测试

## 开发约定
- 仅最小化实现，按需引入依赖（extras）。
- 单元测试仅覆盖改动部分。
- 禁止改动 `.env`。

## 依赖管理策略
- 使用版本范围限制：`>=x.y.z,<x.y+1.0` 格式
- 防止破坏性更新，允许安全补丁更新
- 保持构建可重现性

## 开发环境安装
```bash
# 安装开发依赖
uv sync --extra dev

# 安装测试依赖
uv sync --extra test

# 安装所有开发测试依赖
uv sync --extra all-dev

# 安装特定 LLM 提供商依赖
uv sync --extra openai
```

## TODO 记录
- 初始化包与发布配置
- 实现统一 Client（OpenAI/Anthropic/Gemini）
- 增加 provider 适配层与最小集成测试
