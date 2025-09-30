from ordeq import node

from resources.catalog.catalogs import inconsistent

catalog = inconsistent


@node(inputs=catalog.hello, outputs=catalog.result)
def func(hello: str) -> str:
    return f"{hello.upper()}!"
