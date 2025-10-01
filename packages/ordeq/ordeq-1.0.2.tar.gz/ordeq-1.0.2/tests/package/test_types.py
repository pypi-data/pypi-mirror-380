import doctest

from ordeq import types


def test_doc(doctest_namespace):
    doctest.testmod(types, globs=doctest_namespace)
