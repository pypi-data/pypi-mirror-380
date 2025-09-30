from ordeq import node
from ordeq.framework import get_node
from ordeq_common import StringBuffer

x = StringBuffer("x")
y = StringBuffer("y")
z = StringBuffer("z")
one = StringBuffer("1")


@node(inputs=[x, y], outputs=[z, one], tags=[])
def func1(x: str, y: str) -> tuple[str, str]:
    return f"{x} + {y}", y


node1 = get_node(func1)
print(node1.tags)


@node(inputs=[x, y], outputs=[z, one], tags=["tag1", "tag2"])
def func2(x: str, y: str) -> tuple[str, str]:
    return f"{x} + {y}", y


node2 = get_node(func2)
print(node2)
print(node2.tags)


@node(inputs=[x, y], outputs=[z, one], tags={"key1": "value1"})
def func3(x: str, y: str) -> tuple[str, str]:
    return f"{x} + {y}", y


node3 = get_node(func3)
print(node3.tags)


@node(inputs=[x, y], outputs=[z, one], tags=None)
def func4(x: str, y: str) -> tuple[str, str]:
    return f"{x} + {y}", y


node4 = get_node(func4)
print(node4.tags)
