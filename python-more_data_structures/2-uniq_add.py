#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_numbers = set(my_list)
    result = 0

    for num in unique_numbers:
        result += num

    return result
