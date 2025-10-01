from ordeq import node, run
from ordeq_common import StringBuffer


@node(outputs=StringBuffer())
def func1() -> str:
    return "Hello"


@node(outputs=StringBuffer())
def func2() -> str:
    return "world"


run(func1, func2, verbose=True)
