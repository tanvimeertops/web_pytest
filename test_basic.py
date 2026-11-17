def add(a,b):
    return a + b

def test_positive_num():
    assert add(2, 3) == 5

def test_negative_num():
    assert add(-2, -3) == -5