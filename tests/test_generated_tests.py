import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from codes.calculator import add, divide
import pytest

def test_add_normal():
    assert add(2, 3) == 5
    assert add(-1, 4) == 3
    assert add(0, 0) == 0

def test_add_edge_cases():
    assert add(2 ** 31 - 1, 1) == (2 ** 31) - 1
    assert add(-(2 ** 31), 1) == -(2 ** 31)
    assert add(2 ** 31, 1) == float('inf')
    assert add(-2 ** 31, -1) == -float('inf')

def test_add_invalid_inputs():
    with pytest.raises(TypeError):
        add("a", "b")
    with pytest.raises(TypeError):
        add([1, 2, 3], [4, 5])

def test_divide_normal():
    assert divide(8, 2) == 4
    assert divide(-8, 2) == -4
    assert divide(10, 2) == 5

def test_divide_edge_cases():
    with pytest.raises(ValueError):
        divide(8, 0)
    assert divide(8, -2) == -4
    assert divide(-8, -2) == 4

def test_divide_invalid_inputs():
    with pytest.raises(TypeError):
        divide("a", "b")
    with pytest.raises(TypeError):
        divide([1, 2], [3])