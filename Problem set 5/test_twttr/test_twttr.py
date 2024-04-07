from twttr import shorten

def test_capital():
    assert shorten('HELLO') == 'HLL'

def test_small():
    assert shorten('twitter') == 'twttr'

def test_punctuations():
    assert shorten("Hello, what's your name") == "Hll, wht's yr nm"

def test_numbers():
    assert shorten('CS50') == 'CS50'
