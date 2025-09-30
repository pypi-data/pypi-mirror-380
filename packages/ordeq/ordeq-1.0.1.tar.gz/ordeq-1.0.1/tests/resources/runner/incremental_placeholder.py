from ordeq import IO, Input, Output, node
from ordeq.framework.runner import run
from ordeq_common import StringBuffer

I1 = Input[str]()
I2 = Input[str]()
O1 = IO[str]()
O2 = Output[str]()


@node(inputs=[I1, I2], outputs=O1)
def f(i: str, j: str) -> str:
    return f"{i} {j}"


@node(inputs=O1, outputs=O2)
def g(a: str) -> str:
    return f(a, a)


print(run(f, g, verbose=True))  # raises NotImplementedError
