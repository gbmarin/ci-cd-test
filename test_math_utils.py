from math_utils import add

def test_add():
    assert add(2, 3) == 5

def test_add_zeros():
    assert add(0, 0) == 0

def test_add_negative():
    assert add(-1, -1) == -2

def test_add_mixed():
    assert add(-1, 5) == 4
