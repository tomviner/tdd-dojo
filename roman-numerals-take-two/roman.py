"""
Roman Numerals

Write a function to convert from normal numbers to Roman Numerals: e.g.
 1  => I
 4  => IV
 7  => VII
10  => X
99  => XCIX
"""

LOOKUP_NUMERALS = (
    (1000, 'M'),
    (900, 'CM'),
    (500, 'D'),
    (400, 'CD'),
    (100, 'C'),
    (90, 'XC'),
    (50, 'L'),
    (40, 'XL'),
    (10, 'X'),
    (9, 'IX'),
    (5, 'V'),
    (4, 'IV'),
    (1, 'I'),
)

def to_roman(num):
    for digit, letter in LOOKUP_NUMERALS:
        if num >= digit:
            return letter + (to_roman(num - digit) or '')
