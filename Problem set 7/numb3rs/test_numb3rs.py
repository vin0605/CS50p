from numb3rs import validate

def main():
    test_range()
    test_format()

def test_range():
    assert validate(r'1000.0.0.0') == False
    assert validate(r'0.1000.0.0') == False
    assert validate(r'0.0.1000.0') == False
    assert validate(r'0.0.0.1000') == False
    assert validate(r'0.0.0.0') == True
    assert validate(r'255.255.255.255') == True
    assert validate(r'1000.1000.1000.1000') == False
    assert validate(r'75.456.76.65') == False

def test_format():
    assert validate(r'lol') == False
    assert validate(r'1') == False
    assert validate(r'1.2') == False
    assert validate(r'1.2.3') == False
    assert validate(r'1.2.3.4') == True

if __name__ == "__main__":
    main()
