from ordeq import node
from ordeq_common import Static, StringBuffer


@node(inputs=[Static(["y", "z"])], outputs=StringBuffer("y"))
def func(x: str) -> str:
    return x
