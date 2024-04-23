from jar import Jar
import pytest

def test_capacity():
    with pytest.raises(ValueError):
        cookie  = Jar(-1)
        cookie = Jar('dog')
    
    cookie = Jar(10)
    assert cookie.capacity == 10
    assert cookie.size == 0

    cookie = Jar(0)
    assert cookie.capacity == 0
    assert cookie.size == 0

def test_str():
    cookie = Jar()
    assert str(cookie) == ''

    cookie.deposit(12)
    assert str(cookie) == '🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪'

def test_deposit():
    cookie = Jar()
    with pytest.raises(ValueError):
        cookie.deposit(13)
        cookie.deposit(-1)
        cookie.deposit('dog')
    cookie.deposit(2)
    assert cookie.size == 2
    cookie.deposit(3)
    assert cookie.size == 5

def test_withdraw():
    cookie = Jar()
    with pytest.raises(ValueError):
        cookie.withdraw(-1)
        cookie.withdraw('dog')
        cookie.withdraw(1)

    cookie.deposit(10)
    cookie.withdraw(5)
    assert cookie.size == 5
    with pytest.raises(ValueError):
        cookie.withdraw(6)
    cookie.withdraw(5)
    assert cookie.size == 0