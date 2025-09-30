import copy

import pytest
from ordeq import Node, node
from ordeq.framework import get_node
from ordeq.framework.graph import NodeGraph
from ordeq.framework.runner import _run_graph, _run_node, run
from ordeq_common import StringBuffer

A, B, D = [StringBuffer(c) for c in "ABD"]
C = StringBuffer()
E = StringBuffer()
F = StringBuffer()


def test_run_regular_node():
    Bp = copy.copy(B)
    Bp.unpersist()
    node = Node(inputs=(A,), outputs=(Bp,), func=lambda x: x + x)
    computed = _run_node(node, hooks=())
    assert computed[Bp] == "AA"


def test_run_node_returns_none():
    node = Node(inputs=(A,), outputs=(), func=lambda _: None)
    computed = _run_node(node, hooks=())
    assert computed == {}


def test_run_node_with_zero_inputs():
    Bp = copy.copy(B)
    Bp.unpersist()
    node = Node(inputs=(), outputs=(Bp,), func=lambda: "something")
    loaded = {Bp: "something"}
    computed = _run_node(node, hooks=())
    assert loaded == computed


def test_run_node_with_zero_inputs_and_outputs():
    node = Node(inputs=(), outputs=(), func=lambda: print("Hello!"))
    loaded = {}
    computed = _run_node(node, hooks=())
    assert loaded == computed


plus = node(func=lambda x, y: f"{x} + {y}", inputs=(A, B), outputs=(C,))
minus = node(func=lambda x, y: f"{x} - {y}", inputs=(C, D), outputs=(E,))
square = node(func=lambda x: f"({x})^2", inputs=(E,), outputs=(F,))


@pytest.mark.parametrize(
    ("nodes", "expected_data_store"),
    [
        (
            [get_node(plus), get_node(minus), get_node(square)],
            {
                C: "A + BAAsomething",
                E: "A + BAAsomething - D",
                F: "(A + BAAsomething - D)^2",
            },
        ),
        (
            [get_node(plus), get_node(minus)],
            {C: "A + BAAsomething", E: "A + BAAsomething - D"},
        ),
        ([get_node(plus)], {C: "A + BAAsomething"}),
    ],
)
def test_run_graph(nodes, expected_data_store):
    data_store = _run_graph(NodeGraph.from_nodes(nodes))
    assert data_store == expected_data_store


@pytest.mark.parametrize(
    ("nodes", "expected_data_store"),
    [
        (
            (plus, minus, square),
            {
                C: "A + BAAsomething",
                E: "A + BAAsomething - D",
                F: "(A + BAAsomething - D)^2",
            },
        ),
        ((plus, minus), {C: "A + BAAsomething", E: "A + BAAsomething - D"}),
        ((plus,), {C: "A + BAAsomething"}),
    ],
)
def test_run_parametrized(nodes, expected_data_store):
    data_store = run(*nodes)
    assert data_store == expected_data_store
