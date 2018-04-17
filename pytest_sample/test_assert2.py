#pytest -s test_assert2.py
#https://docs.pytest.org/en/latest/assert.html
import pytest

#ゼロ除算エラーになることを確認
def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        1 / 0

#エラーにならなかったので逆にエラーになる
def test_zero_division2():
    with pytest.raises(ZeroDivisionError):
        1 / 1


def test_recursion_depth():
    with pytest.raises(RuntimeError) as excinfo:
        def f():
            f()
        f()
    assert 'maximum recursion' in str(excinfo.value)


import pytest

def myfunc():
    raise ValueError("Exception 123 raised")

def test_match():
    with pytest.raises(ValueError, match=r'.* 123 .*'):
        myfunc()

