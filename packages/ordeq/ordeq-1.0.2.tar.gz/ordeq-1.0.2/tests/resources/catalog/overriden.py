from ordeq import node, run

from resources.catalog.catalogs import remote_extended

catalog = remote_extended


@node(inputs=catalog.hello, outputs=catalog.another_io)
def func1(hello: str) -> str:
    return f"{hello.upper()}!"


print(run(func1))
