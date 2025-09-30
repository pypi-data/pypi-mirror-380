from collections.abc import Callable
from typing import TypeGuard

Pipeline = set[Callable]

"""
A pipeline represents a set of nodes. Example usage:

```python
>>> # in reference/to.py
>>> from ... import node1, node2
>>> pipeline: Pipeline = {node1, node2}
```

Pipelines can be used to run a set of nodes through the Ordeq CLI, like so:

```shell
$ python {your-entrypoint} run \
    --pipeline {reference}.{to}:{pipeline}
```

You can also run multiple pipelines together, like so:

```shell
$ python {your-entrypoint} run \
    --pipeline {reference}.{to}:{pipeline1} \
    {reference}.{to}:{pipeline2}
```

Ordeq will resolve the dependencies between nodes in the pipelines.

Lastly, it is possible to run a combination of nodes and pipelines:

```shell
$ python {your-entrypoint} run \
    --pipeline {reference}.{to}:{pipeline} \
    --node {reference}.{to}:{node}
```

You can also run the pipeline programmatically as follows:

```python
>>> # in reference/to.py
>>> from reference.to import pipeline
>>> from ordeq.framework.runner import run
>>> run(*pipeline)
```

Pipelines are sets, so any set operation works on pipelines:

```python
>>> run(*pipeline1.union(pipeline2))
```

"""


def is_pipeline(obj: object) -> TypeGuard[Pipeline]:
    """Returns whether an object is a pipeline, meaning a set of nodes. Used
    because ``isinstance`` cannot be used on generic type ``set[Node]``.

    Args:
        obj: the object

    Returns:
        whether ``obj`` is a pipeline or not
    """

    return isinstance(obj, set) and all(callable(o) for o in obj)
