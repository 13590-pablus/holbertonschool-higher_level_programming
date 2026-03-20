#!/usr/bin/python3
"""
This module defines a function that prints a square with the character #.
"""

def print_square(size):
    """
    Prints a square with '#' characters of given size.

    Args:
        size (int): size of the square

    Raises:
        TypeError: if size is not an integer
        ValueError: if size < 0
    """
    # check type
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    # check value
    if size < 0:
        raise ValueError("size must be >= 0")

    # print square
    for _ in range(size):
        print("#" * size)
