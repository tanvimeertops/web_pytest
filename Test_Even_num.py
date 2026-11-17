import pytest

def is_even(num):
    return num % 2 == 0


@pytest.mark.parametrize("num, expected", [
    (2,True),
    (3,False),  
    (4,True),
    (5,False)
])
def test_is_even(num, expected):
    assert is_even(num) == expected