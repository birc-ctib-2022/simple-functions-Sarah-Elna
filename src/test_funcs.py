# This directory will be checked with pytest. It will examine
# all files that start with test_*.py and run all functions with
# names that start with test_

from funcs import (
    prod,
    prod2,
    longest,
    dist
)

from math import sqrt

def test_prod():
    assert prod(1, 2, 3) == 6


def test_prod2():
    assert prod2(2) == 6


def test_longest():
    assert longest([1, 2, 3], [4, 5]) == [1, 2, 3]


def test_dist():
    assert dist((1, 2), (3, 4)) == sqrt(8)
