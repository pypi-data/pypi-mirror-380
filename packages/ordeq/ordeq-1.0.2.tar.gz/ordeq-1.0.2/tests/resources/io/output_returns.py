from dataclasses import dataclass

from ordeq import Output


@dataclass(kw_only=True, frozen=True)
class ExampleOutputNosave(Output):
    def save(self, data: str) -> str:
        return "hello"


_ = ExampleOutputNosave()
