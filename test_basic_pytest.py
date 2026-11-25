def add(a,b):
    return a+b


def test_positive_num():
    assert add(5,3)==8

def test_negative_num():
    assert add(-2,-2)==-4