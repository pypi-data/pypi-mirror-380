# llmhive

[![PyPI](https://img.shields.io/pypi/v/llmhive.svg)](https://pypi.org/project/llmhive/)
[![Python](https://img.shields.io/pypi/pyversions/llmhive.svg)](https://pypi.org/project/llmhive/)
[![License](https://img.shields.io/pypi/l/llmhive.svg)](LICENSE)

**llmhive** 是一个 Python 库，用于以统一的方式调用多种大语言模型（LLM），屏蔽底层 SDK 的差异，支持流式输出和插件式扩展。

## ✨ 特性

- 🚀 统一 API：无论是 OpenAI、Gemini、Ollama 等，都可以用相同的调用方式。
- 📡 支持流式输出：方便做实时响应的应用（如 CLI、聊天机器人、WebSocket 服务）。
- 🧩 插件化：可以很方便地扩展新的模型调用器（Caller）。
- 🔒 类型安全：基于现代 Python 类型提示，开发体验友好。
- 🛠️ 适配 [pyproject.toml] 可选依赖，按需安装。

## 📦 安装

默认安装基础库：

```bash
pip install llmhive
```

安装特定模型支持：

```bash
# OpenAI
pip install llmhive[openai]

# Google Gemini
pip install llmhive[gemini]

# Ollama (本地模型)
pip install llmhive[ollama]
```

## 🚀 快速上手

下面示例展示如何调用 OpenAI ChatGPT，并支持流式输出：

```python
from llmhive.callers.openai_caller import OpenAICaller
from llmhive.message import Message
from llmhive.caller import CallerContext

caller = OpenAICaller(model="gpt-4o-mini")

ctx = CallerContext(
    system_prompt="You are a helpful assistant.",
    history=[
        Message(role="user", content="Hello!"),
    ],
    is_stream=True,
)

for chunk in caller.call(ctx):
    print(chunk, end="", flush=True)
```

## 🌐 支持的模型提供商

| Provider | Extra Dependency          | Example Caller |
| -------- | ------------------------- | -------------- |
| OpenAI   | `pip install llmhive[openai]` | `OpenAICaller` |
| Gemini   | `pip install llmhive[gemini]` | `GeminiCaller` |
| Ollama   | `pip install llmhive[ollama]` | `OllamaCaller` |

未来计划支持：Anthropic Claude、Mistral、AWS Bedrock 等。

## 🧩 扩展新模型

要支持新的 LLM，只需继承 `Caller` 基类，实现 `call` 方法：

```python
from llmhive.caller import Caller, CallerContext
from collections.abc import Iterator

class MyLLMCaller(Caller):
    def __init__(self, model: str):
        self.model = model

    def call(self, ctx: CallerContext) -> Iterator[str]:
        # 这里实现你的模型调用逻辑
        yield "Hello from MyLLM!"
```

然后就可以像内置的 Caller 一样使用它。

## 📖 开发

克隆仓库：

```bash
git clone https://github.com/yourname/llmhive.git
cd llmhive
```

安装依赖：

```bash
pip install -e '.[openai,gemini,ollama]'
```

运行测试：

```bash
pytest
```

## 📜 许可证

本项目基于 [Apache 2.0 License](LICENSE) 开源。

---

## 🔗 相关项目

* [OpenAI Python SDK](https://github.com/openai/openai-python)
* [Google GenAI SDK](https://pypi.org/project/google-genai/)
* [Ollama](https://ollama.ai)
