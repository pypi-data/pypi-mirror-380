from types import ModuleType

from ordeq import node, run

from resources.catalog.catalogs import local, remote

catalog: ModuleType = local


@node(inputs=catalog.hello, outputs=catalog.result)
def func1(hello: str) -> str:
    return f"{hello.upper()}!"


print(run(func1))

catalog: ModuleType = remote


@node(inputs=catalog.hello, outputs=catalog.result)
def func2(hello: str) -> str:
    return f"{hello.upper()}!"


print(run(func2))
