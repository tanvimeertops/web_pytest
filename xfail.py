import pytest
def div(a,b):
    return a/b

@pytest.mark.xfail(reason="num cannot divide by 0")
def test_div_by_zero():
    div(4,0)==0

@pytest.mark.xfail(reason="known bug")
def test_sub():
    result=5-3
    assert result==1
