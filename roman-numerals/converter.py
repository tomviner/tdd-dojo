def roman_converter(number):
    numeral = 'I' * (number % 5)
    if number <= 4:
        return numeral
    if number >= 5 and number < 10:
        return 'V' + numeral
    if number >= 10:
        return 'X' + numeral
