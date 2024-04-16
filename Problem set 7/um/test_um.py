from um import count


def test_zero():
    assert count("hello world") == 0
    assert count("yummy") == 0
    assert count("umum") == 0

def test_normal():
    assert count("hello, um, world") == 1
    assert count("um um um") == 3

def test_punctuations():
    assert count("um?") == 1
    assert count("Um, thanks for the album.") == 1
    assert count("Um, thanks, um...") == 2
    assert count("um....") == 1
