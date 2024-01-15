import pytest
from devine_steve import *

resultat = devine()

def test_decomposer_steve():
    assert decomposer(123) == (1,2,3)
    assert decomposer(456) == (4,5,6)

def test_divisible_steve():
    assert divisible(99)
    assert divisible(81)
    assert not divisible(100)

def test_somme_steve():
    assert somme(5,2,3)
    assert not somme(4,5,6)

def test_devine_steve():
    assert devine() == resultat
