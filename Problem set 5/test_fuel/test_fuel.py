from fuel import convert, gauge
import pytest


def test_incorrect_input():
    with pytest.raises(ValueError):
        convert('cat/dog')

def test_incorrect_input2():
    with pytest.raises(ValueError):
        convert('4/3')

def test_zerodivision():
    with pytest.raises(ZeroDivisionError):
        convert('1/0')

def test_normal():
    assert convert('2/4') == 50

def test_one():
    assert convert('1/100') == 1

def test_99():
    assert convert('99/100') == 99

def test_gauge_empty():
    assert gauge(1) == 'E'

def test_gauge_full():
    assert gauge(99) == 'F'

def test_gauge_normal():
    assert gauge(50) == '50%'

