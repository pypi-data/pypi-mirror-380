from types import ModuleType
from unittest.mock import Mock

import pytest
from ordeq.framework.catalog import CatalogError, check_catalogs_are_consistent
from ordeq_common import Static, StringBuffer


@pytest.mark.parametrize(
    ("a", "b"),
    [
        (
            {
                # empty
            },
            {
                # empty
            },
        ),
        (
            {
                # empty
            },
            {
                "something_else": 4  # not an IO
            },
        ),
        ({"hello": StringBuffer()}, {"hello": Static("hello")}),
        (
            {"hello": StringBuffer(), "result": StringBuffer()},
            {
                "hello": Static("hello"),
                "result": StringBuffer(),
                "something_else": 4,  # not an IO
            },
        ),
    ],
)
def test_it_checks_consistent(a, b):
    catalog_a = Mock(ModuleType)
    catalog_b = Mock(ModuleType)
    catalog_a.__dict__ = a
    catalog_b.__dict__ = b
    check_catalogs_are_consistent(catalog_a, catalog_b)


@pytest.mark.parametrize(
    ("a", "b"),
    [
        (
            {"hello": StringBuffer(), "result": StringBuffer()},
            {
                "hello": Static("hello")
                # result is mising
            },
        ),
        (
            {
                "hello": StringBuffer()
                # result is missing
            },
            {"hello": Static("hello"), "result": StringBuffer()},
        ),
        (
            {
                # empty
            },
            {"hello": Static("hello")},
        ),
        (
            {
                # empty but contains non-IO
                "something_else": 4
            },
            {"hello": Static("hello"), "result": StringBuffer()},
        ),
    ],
)
def test_it_checks_inconsistent(a, b):
    catalog_a = Mock(ModuleType)
    catalog_b = Mock(ModuleType)
    catalog_a.__dict__ = a
    catalog_b.__dict__ = b
    with pytest.raises(CatalogError, match="Catalogs are inconsistent"):
        check_catalogs_are_consistent(catalog_a, catalog_b)
