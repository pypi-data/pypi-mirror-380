import base64
import os
from typing import Iterator, Optional, cast
from ..errors import MissingAPIKeyError, MissingDependencyError
from ..caller import Caller, CallerContext
from ..message import Message

try:
    from openai import OpenAI, Stream
    from openai.types.chat import ChatCompletion, ChatCompletionMessageParam, ChatCompletionChunk, ChatCompletionContentPartParam
except ImportError as e:
    raise MissingDependencyError(
        "OpenAICompatibleCaller requires `openai`. Please install it with: pip install llm-caller[openai]"
    ) from e


class OpenAICaller(Caller):
    def __init__(self, model: str, base_url = "https://api.openai.com/v1/responses"):
        api_key = os.getenv("API_KEY_OPEANAI")
        if not api_key:
            raise MissingAPIKeyError(
                "OpenAICaller requires the API key. Please set the API_KEY_OPEANAI environment variable."
            )
        self.client: Optional[OpenAI] = None
        self.init(model, api_key, base_url)

    def init(self, model: str, api_key: str, base_url: str):
        self.model = model
        self.client = OpenAI(
            api_key=api_key,
            base_url=base_url,
        )

    def call(self, ctx: CallerContext) -> Iterator[str]:
        if self.client is None:
            raise ValueError("OpenAICaller is not initialized properly.")
        openai_messages: list[ChatCompletionMessageParam] = []
        openai_messages.append({"content": ctx.system_prompt, "role": "system"})
        if ctx.history:
            openai_messages.extend([self._build_message_content(message) for message in ctx.history])
        openai_messages.append(self._build_message_content(ctx.get_user_prompt()))
        response = self.client.chat.completions.create(
            messages=openai_messages,
            model=self.model,
            n=1,
            stream=ctx.is_stream,
            # extra_body=extra_body,
        )
        if ctx.is_stream:
            stream = cast(Stream[ChatCompletionChunk], response)
            for chunk in stream:
                delta = chunk.choices[0].delta.content
                if delta:
                    yield delta
        else:
            completion = cast(ChatCompletion, response)
            yield completion.choices[0].message.content or ""

    def _build_message_content(self, message: Message) -> ChatCompletionMessageParam:
        if message.role == "user":
            content: list[ChatCompletionContentPartParam] = []
            if message.images:
                for image_path in message.images:
                    with open(image_path, "rb") as image_file:
                        base64_image = base64.b64encode(image_file.read()).decode("utf-8")
                        content.append(
                            {
                                "type": "image_url",
                                "image_url": {
                                    "url": f"data:image/jpeg;base64,{base64_image}"
                                },
                            }
                        )
                content.append({"type": "text", "text": message.content})
            return {"content": content, "role": "user"}
        elif message.role == "assistant":
            return {"content": message.content, "role": "assistant"}
        else:
            raise ValueError(f"Unknown message role: {message.role}")


class BailianCaller(OpenAICaller):
    TURBO = "qwen-turbo"
    FREE = "qwen2.5-1.5b-instruct"

    def __init__(self, model: str):
        api_key = os.getenv("API_KEY_BAILIAN")
        if not api_key:
            raise MissingAPIKeyError(
                "BailianCaller requires the API key. Please set the API_KEY_BAILIAN environment variable."
            )
        self.client: Optional[OpenAI] = None
        super().init(model, api_key, "https://dashscope.aliyuncs.com/compatible-mode/v1")


class HunyuanCaller(OpenAICaller):
    TURBO = "hunyuan-turbo"
    FREE = "hunyuan-lite"

    def __init__(self, model: str):
        api_key = os.getenv("API_KEY_HUNYUAN")
        if not api_key:
            raise MissingAPIKeyError(
                "HunyuanCaller requires the API key. Please set the API_KEY_HUNYUAN environment variable."
            )
        self.client: Optional[OpenAI] = None
        super().init(model, api_key, "https://api.hunyuan.cloud.tencent.com/v1")


class XinghuoCaller(OpenAICaller):
    FREE = "lite"

    def __init__(self, model: str):
        api_key = os.getenv("API_KEY_XINGHUO")
        if not api_key:
            raise MissingAPIKeyError(
                "XinghuoCaller requires the API key. Please set the API_KEY_XINGHUO environment variable."
            )
        self.client: Optional[OpenAI] = None
        super().init(model, api_key, "https://spark-api-open.xf-yun.com/v1")


class ModelScopeCaller(OpenAICaller):
    QWEN2_5_CODER_32B = "Qwen/Qwen2.5-Coder-32B-Instruct"
    DEEPSEEK_V3 = "deepseek-ai/DeepSeek-V3-0324"
    QWEN3_8B = "Qwen/Qwen3-8B"
    QWEN3_14B = "Qwen/Qwen3-14B"

    def __init__(self, model: str):
        api_key = os.getenv("API_KEY_MODELSCOPE")
        if not api_key:
            raise MissingAPIKeyError(
                "ModelScopeCaller requires the API key. Please set the API_KEY_MODELSCOPE environment variable."
            )
        self.client: Optional[OpenAI] = None
        super().init(model, api_key, "https://api-inference.modelscope.cn/v1/")
