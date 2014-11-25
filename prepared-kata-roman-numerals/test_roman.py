import pytest

from roman import *
from acceptance_test_values import ACCEPTANCE_TEST_PACK

TEST_PAIRS_1 = (
    (1, 'I'),
    (5, 'V'),
    (10, 'X'),
    (50, 'L'),
)
TEST_PAIRS_2 = TEST_PAIRS_1 + (
)
TEST_PAIRS_3 = TEST_PAIRS_2 + (
    (6, 'VI'),
    (11, 'XI'),
    (16, 'XVI'),
    (51, 'LI'),
    (55, 'LV'),
    (60, 'LX'),
    (66, 'LXVI'),
)
TEST_PAIRS_4 = TEST_PAIRS_3 + (
    (2, 'II'),
    (8, 'VIII'),
    (33, 'XXXIII'),
    (88, 'LXXXVIII'),
)
TEST_PAIRS_5 = TEST_PAIRS_4 + (
    (4, 'IV'),
    (9, 'IX'),
    (24, 'XXIV'),
    (89, 'LXXXIX'),
)
TEST_PAIRS_FULL = TEST_PAIRS_5 + (
    (90, 'XC'),
    (93, 'XCIII'),
    (99, 'XCIX'),
    (143, 'CXLIII'),
    (3888, 'MMMDCCCLXXXVIII'),
    (3940, 'MMMCMXL'),
    (3999, 'MMMCMXCIX'),
) + ACCEPTANCE_TEST_PACK

@pytest.mark.parametrize('num,roman', TEST_PAIRS_1)
def test_roman_1(num, roman):
    assert to_roman_1(num) == roman

@pytest.mark.parametrize('num,roman', TEST_PAIRS_2)
def test_roman_2(num, roman):
    assert to_roman_2(num) == roman

@pytest.mark.parametrize('num,roman', TEST_PAIRS_3)
def test_roman_3(num, roman):
    assert to_roman_3(num) == roman

@pytest.mark.parametrize('num,roman', TEST_PAIRS_4)
def test_roman_4(num, roman):
    assert to_roman_4(num) == roman

@pytest.mark.parametrize('num,roman', TEST_PAIRS_5)
def test_roman_5(num, roman):
    assert to_roman_5(num) == roman

@pytest.mark.parametrize('num,roman', TEST_PAIRS_FULL)
def test_roman_6(num, roman):
    assert to_roman_6(num) == roman

@pytest.mark.parametrize('num,roman', TEST_PAIRS_FULL)
def test_roman_7(num, roman):
    assert to_roman_7(num) == roman
