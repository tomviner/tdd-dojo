"""
Problem desc:

"""
DIGIT_MAP = (
    (100, 'C'),
    # (90, 'XC'),
    (50, 'L'),
    (10, 'X'),
    (5, 'V'),
    # (4, 'IV'),
    (1, 'I'),
)


# def to_roman(num):
#     result = ''
#     remainder = num
#     for arabic, roman in DIGIT_MAP:
#         while remainder >= arabic:
#             # if num == arabic:
#             result += roman
#             remainder -= arabic
#     return result


def to_roman(num):
    result = ''
    if num == 5:
        result = 'V'
    if num == 1:
        result = 'I'
    return result