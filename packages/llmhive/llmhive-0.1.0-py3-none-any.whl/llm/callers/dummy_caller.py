from typing import Iterator
from ..caller import Caller, CallerContext


class DummyCaller(Caller):
    def call(self, ctx: CallerContext) -> Iterator[str]:
        yield "dummy"
