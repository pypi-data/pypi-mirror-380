import resources.runner.example_module_a as example_module_a
from ordeq import run, node


@node
def noop() -> None:
    return


run(example_module_a, noop, verbose=True)
