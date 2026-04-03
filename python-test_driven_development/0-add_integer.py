#!/usr/bin/python3
"""
This module contains a function that adds two integers.
"""

def add_integer(a, b=98):
    """Adds two integers or floats.
    
    Args:
        a: first number
        b: second number, defaults to 98
        
    Returns:
        The addition of a and b as an integer.
        
    Raises:
        TypeError: If a or b is not an integer or float.
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
        
    return int(a) + int(b)
