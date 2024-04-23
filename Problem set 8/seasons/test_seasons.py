from seasons import min_calculator

def test_normal():
    assert min_calculator(365) == "Five hundred twenty-five thousand, six hundred minutes"
    assert min_calculator(10000) == 'Fourteen million, four hundred thousand minutes'