from bank import value

def test_zero():
    assert value('hello') ==  0
    assert value('hello newman') == 0
    assert value('HELLO NEWMAN') == 0
    assert value('Hello, newman') == 0

def test_twenty():
    assert value('hi') ==  20
    assert value('hi newman') == 20
    assert value('Hi NEWMAN') == 20
    assert value('Hi, newman') == 20

def test_hundred():
    assert value('lol') == 100
    assert value('nihao') == 100
