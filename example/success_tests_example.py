import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from calculator import add, divide
import pytest

def test_add_normal():
    assert add(2, 3) == 5

def test_add_edge():
    assert add(-10, 0) == -10
    assert add(0, 10) == 10
    assert add(-10, 10) == 0

def test_add_invalid_inputs():
    with pytest.raises(TypeError):
        add("str", 5)
    with pytest.raises(TypeError):
        add(5, "str")

def test_divide_normal():
    assert divide(10, 2) == 5.0

def test_divide_edge():
    assert divide(-10, -2) == 5.0
    assert divide(5, -2) == -2.5

def test_divide_zero_division():
    with pytest.raises(ValueError):
        divide(10, 0)

def test_divide_invalid_inputs():
    with pytest.raises(TypeError):
        divide("str", 5)
    with pytest.raises(TypeError):
        divide(5, "str")