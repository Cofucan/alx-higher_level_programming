#!/usr/bin/python3

def roman_to_int(roman_string):
    if type(roman_string) != str or roman_string is None:
        return 0

    numerals = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
            }

    # If any character from the string is not a valid roman numeral
    if any(c not in numerals for c in roman_string):
        return 0

    # Get the value of the first numeral
    rnum = numerals[roman_string[0]]

    # Iterate over each numeral after the first numeral
    for i, s in enumerate(roman_string[1:], 1):
        # If the previous numeral is less than the current numeral
        if numerals[roman_string[i-1]] < numerals[roman_string[i]]:
            rnum += numerals[roman_string[i]] - 2*(numerals[roman_string[i-1]])
        else:
            rnum += numerals[s]

    return rnum
