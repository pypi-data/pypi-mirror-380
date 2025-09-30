import os

from ordeq import node, run

from resources.catalog.catalogs import local, remote

os.environ["ENV"] = "local"


def get_catalog():
    return local if os.environ["ENV"] == "local" else remote


catalog = get_catalog()


@node(inputs=catalog.hello, outputs=catalog.result)
def func1(hello: str) -> str:
    return f"{hello.upper()}!"


print(run(func1))

os.environ["ENV"] = "acceptance"
catalog = get_catalog()


@node(inputs=catalog.hello, outputs=catalog.result)
def func2(hello: str) -> str:
    return f"{hello.upper()}!"


print(run(func2))
