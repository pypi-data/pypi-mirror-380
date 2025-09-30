from ordeq import node
from ordeq.framework.runner import run
from ordeq_common import Static, StringBuffer

x1 = Static(1)
x2 = StringBuffer()
x3 = StringBuffer()


@node(inputs=x1, outputs=x2)
def increment(x: int) -> str:
    return f"{x + 1}"


@node(inputs=[x2, x1], outputs=x3)
def decrement(x: str, y: str) -> str:
    return f"{int(x) - int(y)}"


regular = run(increment, decrement, verbose=True)

print(regular)

# provide alternative IO when running the pipeline
patched = run(increment, decrement, io={x1: Static(200)}, verbose=True)

print(patched)
