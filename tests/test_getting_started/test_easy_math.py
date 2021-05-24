from getting_started.easy_math import sum, subtract

def test_sum():
    assert sum(3, 2) == 5
    assert sum(10, 7) == 17
    assert sum(100, -107) == -7

def test_subtract():
    assert subtract(3,1) == 2
    assert subtract (100, 49) == 51
    assert subtract (100, -49) == 149
    assert subtract (-100, -107) == 7