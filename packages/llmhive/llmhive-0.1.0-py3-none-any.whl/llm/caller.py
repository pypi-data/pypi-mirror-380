from dataclasses import dataclass
from typing import Any, Iterator, Optional, Protocol
from pydantic import BaseModel

from .message import Message


class UserPrompt(BaseModel):
    content: str
    images: Optional[list[str]] = None


@dataclass
class CallerContext:
    user_prompt: str | UserPrompt
    system_prompt: str = "You are a helpful assistant."
    history: Optional[list[Message]] = None
    is_stream: bool = False
    is_json: bool = False
    extra_body: Optional[dict[str, Any]] = None

    def get_user_prompt(self) -> Message:
        if isinstance(self.user_prompt, str):
            return Message(role="user", content=self.user_prompt)
        return Message(role="user", content=self.user_prompt.content, images=self.user_prompt.images)

    def get_system_prompt(self) -> Message:
        return Message(role="system", content=self.system_prompt)


class Caller(Protocol):

    def call(self, ctx: CallerContext) -> Iterator[str]:
        ...


class CallerFactory:
    @classmethod
    def create(cls, model: str, provider: Optional[str] = None) -> Caller:
        if provider == "modelscope":
            from .callers.openai_caller import ModelScopeCaller
            return ModelScopeCaller(model)
        if provider == "ollama":
            from .callers.ollama_caller import OllamaCaller
            return OllamaCaller(model)
        if provider == "xinghuo":
            from .callers.openai_caller import XinghuoCaller
            return XinghuoCaller(model)
        if model == "dummy":
            from .callers.dummy_caller import DummyCaller
            return DummyCaller()
        elif model.startswith("gemini"):
            from .callers.gemini_caller import GeminiCaller
            return GeminiCaller(model)
        elif model.startswith("qwen"):
            from .callers.openai_caller import BailianCaller
            return BailianCaller(model)
        elif model.startswith("hunyuan"):
            from .callers.openai_caller import HunyuanCaller
            return HunyuanCaller(model)
        raise ValueError(f"Unknown model: {model}")
