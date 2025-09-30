import pytest
from ordeq import Node, node
from ordeq.framework.pipeline import Pipeline, is_pipeline
from ordeq_common import StringBuffer

node_1 = node(inputs=(), outputs=(), func=lambda: None)
node_2 = node(inputs=(), outputs=(StringBuffer(),), func=lambda: "bluh")


@pytest.mark.parametrize(
    ("obj", "expected"),
    [
        (object, False),
        ({}, False),
        ({1, 2, 3}, False),
        ({"a", 1}, False),
        ({"a", node_1}, False),
        ({node_1}, True),
        ({node_1, node_2}, True),
        (Pipeline, False),
        (Node, False),
    ],
)
def test_is_pipeline(obj: object, expected: bool):
    assert is_pipeline(obj) == expected
