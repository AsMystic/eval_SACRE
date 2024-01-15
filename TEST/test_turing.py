import pytest
from devine_turing import *

resultat = devine()

def test_decomposer_turing():
    assert decomposer(123) == (1,2,3)
    assert decomposer(456) == (4,5,6)

def test_divisible_turing():
    assert divisible(99)
    assert divisible(81)
    assert not divisible(100)

def test_somme_turing():
    assert somme(3,6,3)
    assert not somme(4,5,6)

def test_devine_turing():
    assert devine() == resultat
