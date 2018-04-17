# coding: utf-8

def test_5():
    a = (1, 2, 3, 4, 5, 6)
    b = (1, 2, 4, 3, 5, 6)
    assert a == b


def test_6():
    a = [1, 2, 3]
    b = (1, 2, 3)
    assert a == b


def test_7():
    a = {'a': 1, 'b': 2, 'c': 3, 'd': None}
    b = {'a': 1, 'b': 4, 'c': 3}
    assert a == b


def test_8():
    a = set([1, 2, 3])
    b = frozenset([1, 2, 3])
    assert a == b