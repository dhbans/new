import pytest

@pytest.mark.P1
def test_TC1P1():
    a = 10
    b = 10
    assert a == b, "a and b is having diffrent values"


@pytest.mark.P2
def test_TC2P2():
    a = 10
    b = 11
    assert a == b, "a and b is having diffrent values"