#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    str_length = len(roman_string)
    total = 0
    for index, char in enumerate(roman_string):
        is_end = index == str_length - 1
        current_value = roman_values[char]
        if is_end:
            total += current_value
        else:
            next = roman_string[index + 1]
            next_value = roman_values[next]
            if next_value > current_value:
                total -= current_value
            else:
                total += current_value
            # print(f"{index}: {char}-> {current_value}")
    return total
