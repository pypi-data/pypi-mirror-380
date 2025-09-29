import os
from typing import Iterator, Optional
from ..caller import Caller, CallerContext
from ..message import Message
from ..errors import MissingDependencyError, MissingAPIKeyError

try:
    from google import genai
    from google.genai import types
except ImportError as e:
    raise MissingDependencyError(
        "GeminiCaller requires `google-genai`. Please install it with: pip install llm-caller[gemini]"
    ) from e


class GeminiCaller(Caller):
    def __init__(self, model: str):
        api_key = os.getenv("API_KEY_GEMINI")
        if not api_key:
            raise MissingAPIKeyError("GeminiCaller requires the API key. Please set the API_KEY_GEMINI environment variable.")
        self.model = model
        self.client = genai.Client(api_key=api_key)

    def call(self, ctx: CallerContext) -> Iterator[str]:
        system_prompt = ctx.system_prompt
        user_prompt = ctx.get_user_prompt()
        history = ctx.history
        gemini_history = self._build_gemini_history(history)
        chat = self.client.chats.create(
            model=self.model,
            config=types.GenerateContentConfig(
                system_instruction=system_prompt,
                response_mime_type="application/json" if ctx.is_json else None,
            ),
            history=gemini_history,
        )
        if ctx.is_stream:
            for chunk in chat.send_message_stream(message=self._build_message_part(user_prompt)):
                yield chunk.text or ""
        else:
            response = chat.send_message(message=self._build_message_part(user_prompt))
            yield response.text or ""

    def _build_message_content(self, role: str, content: str) -> types.Content:
        return types.Content(
            role="user" if role == "user" else "model",
            parts=[types.Part(text=content)],
        )

    def _build_gemini_history(self, messages: Optional[list[Message]]) -> list[types.ContentOrDict]:
        return [
            self._build_message_content(message.role, message.content)
            for message in messages
        ] if messages else []

    def _build_message_part(self, message: Message) -> list[types.Part]:
        if message.images:
            image_url = message.images[0]
            with open(image_url, "rb") as f:
                image_bytes = f.read()
            return [
                types.Part(text=message.content),
                types.Part.from_bytes(data=image_bytes, mime_type="image/jpeg"),
            ]
        return [types.Part(text=message.content)]
