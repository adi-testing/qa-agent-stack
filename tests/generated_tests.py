import pytest

def test_add_normal():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0.5, 0.5) == 1

def test_add_edgecases():
    assert add(-1000, 1000) == 999
    assert add(1e9, -1e9) == 0
    assert add("a", "b") == "ab"
    assert add([1, 2], [3, 4]) == [1, 2, 3, 4]

def test_add_invalid():
    with pytest.raises(TypeError):
        add(2, "3")
    with pytest.raises(TypeError):
        add([1, 2], "3")
    assert add(None, 3) is None
    assert add("foo", None) is None

def test_divide_normal():
    assert divide(6, 2) == 3.0
    assert divide(-6, -2) == 3.0
    assert divide(4.5, 1.5) == 3.0

def test_divide_edgecases():
    assert divide(-8, 2) == -4.0
    assert divide(0.1, 0) == pytest.raises(ValueError, "Cannot divide by zero.")
    assert divide(1, 0) is pytest.raises(ZeroDivisionError)

def test_divide_invalid():
    with pytest.raises(TypeError):
        divide("a", "b")
    with pytest.raises(TypeError):
        divide([1, 2], [0])
    assert divide(1, None) is pytest.raises(TypeError)