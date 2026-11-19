import pytest
def div(a,b):
    return a/b


def test_div_by_num():
    assert div(100,2)==50

@pytest.mark.xfail(reason="divide by 0 is not handled",strict=True)
def test_div_by_zero():
    assert div(1,0)==0

