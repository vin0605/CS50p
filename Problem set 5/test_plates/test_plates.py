from plates import is_valid

def test_twoletters():
    assert is_valid('CS50') == True
    assert is_valid('W513') == False

def test_length():
    assert is_valid('C') == False
    assert is_valid('CS505050') == False
    assert is_valid('CS505') == True

def test_punctuations():
    assert is_valid('CS50.') == False
    assert is_valid('CS50:') == False

def test_midnum():
    assert is_valid('CS50C') == False

def test_firstnum():
    assert is_valid('CS05') == False
