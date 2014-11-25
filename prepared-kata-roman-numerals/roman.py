from __future__ import print_function
"""
Roman Numerals

Write a function to convert from normal numbers to Roman Numerals: e.g.
 1  => I
 4  => IV
 7  => VII
10  => X
99  => XCIX
"""


# Simple if chain
def to_roman_1(num):
    if num == 50:
        return 'L'
    if num == 10:
        return 'X'
    if num == 5:
        return 'V'
    return 'I'


# Separate data from functionality
# Add print to show what's happening
DIGIT_MAP_2 = (
    (50, 'L'),
    (10, 'X'),
    (5, 'V'),
    (1, 'I'),
)
def to_roman_2(num):
    result = ''
    for digit, letter in DIGIT_MAP_2:
        if num == digit:
            print('{} {}'.format(
                digit, letter
            ))
            result = letter
    return result


# Think about basic algorithm
# remainder!
DIGIT_MAP_3 = (
    (50, 'L'),
    (10, 'X'),
    (5, 'V'),
    (1, 'I'),
)
def to_roman_3(num):
    result = ''
    remainder = num
    for digit, letter in DIGIT_MAP_3:
        if remainder >= digit:

            print('{} - {}({}) = {}'.format(
                remainder, digit, letter, remainder - digit
            ))

            result += letter
            remainder -= digit
    return result


# Keep taking repeat letters that we need
DIGIT_MAP_4 = (
    (50, 'L'),
    (10, 'X'),
    (5, 'V'),
    (1, 'I'),
)
def to_roman_4(num):
    result = ''
    remainder = num
    for digit, letter in DIGIT_MAP_4:
        while remainder >= digit:
            result += letter
            remainder -= digit
    return result


# Special case the subtractions
DIGIT_MAP_5 = (
    (50, 'L'),
    (10, 'X'),
    (5, 'V'),
    (1, 'I'),
)
def to_roman_5(num):
    result = ''
    remainder = num
    for digit, letter in DIGIT_MAP_5:
        while remainder >= digit:
            result += letter
            remainder -= digit
    return result.replace('VIIII', 'IX').replace('IIII', 'IV')


# Generalise the subtractions
# Run full acceptance test pack!
DIGIT_MAP_6 = (
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

def to_roman_6(num):
    result = ''
    remainder = num
    for digit, letter in DIGIT_MAP_6:
        while remainder >= digit:
            result += letter
            remainder -= digit
    return result


# Go recursive
def to_roman_7(num):
    for digit, letter in DIGIT_MAP_6:
        if num >= digit:
            return letter + (
                to_roman_7(num - digit) or ''
            )
