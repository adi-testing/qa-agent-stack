import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from codes.calculator import add, divide
import pytest

def test_add_normal():
    assert add(2, 3) == 5
    assert add(-4, 6) == 2
    assert add(0, 0) == 0

def test_add_edge():
    assert add(1, 2 ** 32) == 2 ** 32 + 1
    assert add(-1 * (2 ** 31), 1) == -2 ** 31
    assert add(-1, 0) == -1

def test_add_empty():
    with pytest.raises(TypeError):
        add(None, 1)
    with pytest.raises(TypeError):
        add(1, None)

def test_add_invalid():
    with pytest.raises(TypeError):
        add("string", 4)

def test_divide_normal():
    assert divide(8, 2) == 4
    assert divide(-8, -2) == 4
    assert divide(10, 2) == 5

def test_divide_edge():
    assert divide(1, 1) == 1
    with pytest.raises(ValueError):
        divide(1, 0)

def test_divide_empty():
    with pytest.raises(TypeError):
        divide(None, 1)
    with pytest.raises(TypeError):
        divide(1, None)

def test_divide_invalid():
    with pytest.raises(ValueError):
        divide(-8, -0)