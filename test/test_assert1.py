# content of test_assert1.py
def f():
    return 3


def test_function():
    assert f() % 2 == 0, "value was odd,should be even"
