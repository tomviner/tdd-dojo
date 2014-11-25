import pytest

from roman import to_roman
from acceptance_test_values import ACCEPTANCE_TEST_PACK

def test_roman_1():
    assert to_roman(1) == 'I'

def test_roman_5():
    assert to_roman(5) == 'V'

def test_roman_10():
    assert to_roman(10) == 'X'

def test_roman_50():
    assert to_roman(50) == 'L'

def test_roman_15():
    assert to_roman(15) == 'XV'

def test_roman_35():
    assert to_roman(35) == 'XXXV'

def test_roman_25():
    assert to_roman(25) == 'XXV'

def test_roman_100():
    assert to_roman(100) == 'C'

def test_roman_1000():
    assert to_roman(1000) == 'M'

def test_roman_500():
    assert to_roman(500) == 'D'

def test_roman_4():
    assert to_roman(4) == 'IV'

def test_roman_9():
    assert to_roman(9) == 'IX'

def test_roman_3999():
    assert to_roman(3999) == 'MMMCMXCIX'

def test_roman_40():
    assert to_roman(40) == 'XL'

def test_roman_400():
    assert to_roman(400) == 'CD'

def test_roman_449():
    assert to_roman(449) == 'CDXLIX'

def test_roman_3888():
    assert to_roman(3888) == 'MMMDCCCLXXXVIII'

@pytest.mark.parametrize("num,expected", ACCEPTANCE_TEST_PACK)
def test_generic_roman(num, expected):
    assert to_roman(num) == expected
