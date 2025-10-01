from ordeq import node
from ordeq_common import StringBuffer, Static

x = Static("X")


@node(inputs=x, outputs=x)  # outputs should be of type Output or IO
def func(data: str) -> str:
    return data + data
