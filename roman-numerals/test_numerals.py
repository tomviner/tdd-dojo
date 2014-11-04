import pytest
from converter import roman_converter


INPUT_OUTPUT = [
    (1, 'I'),
    (2, 'II'),
    (3, 'III'),
    (4, 'IIII'),
    (5, 'V'),
    (6, 'VI'),
    (7, 'VII'),
    (8, 'VIII'),
    (9, 'VIIII'),
    (10, 'X'),
]

@pytest.mark.parametrize('number,expected_output', INPUT_OUTPUT)
def test_convert_list_of_number(number, expected_output):
    assert roman_converter(number) == expected_output
