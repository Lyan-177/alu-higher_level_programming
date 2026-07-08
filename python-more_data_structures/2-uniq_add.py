#!/usr/bin/python3


def uniq_add(my_list=[]):
    """
    Adds all unique integers in a list.
    """
    unique_sum = 0
    unique_numbers = []

    for number in my_list:
        if number not in unique_numbers:
            unique_numbers.append(number)
            unique_sum += number

    return unique_sum
