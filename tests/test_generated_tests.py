import pytest

def test_add_normal():
    assert add(2, 3) == 5
    assert add(-1, 2) == -1
    assert add(0, 0) == 0

def test_add_edge():
    # Test large numbers
    assert add(999999999, 1) == 1000000000
    assert add(-999999999, -1) == -1000000000

    # Test with small numbers close to limits
    assert add(sys.maxsize - 1, 1) == sys.maxsize
    assert add(-sys.maxsize + 1, -1) == -sys.maxsize

def test_add_invalid():
    def _test_add(a, b):
        with pytest.raises(TypeError):
            add('str', 'str')
        with pytest.raises(TypeError):
            add(1.0, 'str')
        with pytest.raises(TypeError):
            add('str', 1.0)
        with pytest.raises(TypeError):
            add([1, 2, 3], 4)
        with pytest.raises(TypeError):
            add(4, [1, 2, 3])

    _test_add(None, 1)
    _test_add(1, None)

def test_divide_normal():
    assert divide(6, 3) == 2.0
    assert divide(-6, 3) == -2.0
    assert divide(-6, -3) == 2.0

def test_divide_edge():
    # Test large numbers close to limits
    assert divide(sys.maxsize, 2) > sys.maxsize / 2 - 1e-7
    assert divide(sys.maxsize, sys.maxsize + 1) < sys.maxsize / (sys.maxsize + 1) + 1e-7

def test_divide_invalid():
    def _test_divide(a, b):
        with pytest.raises(ValueError):
            divide(5, 0)
        with pytest.raises(TypeError):
            divide('str', 'str')
        with pytest.raises(TypeError):
            divide(1.0, 'str')
        with pytest.raises(TypeError):
            divide('str', 1.0)