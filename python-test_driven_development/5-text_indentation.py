#!/usr/bin/python3
"""
This module defines a function that prints text with 2 new lines after
'.', '?' and ':' characters.
"""

def text_indentation(text):
    """
    Prints text with 2 new lines after each '.', '?' and ':'.
    
    Args:
        text (str): text to print

    Raises:
        TypeError: if text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # işarələr: '.', '?', ':'
    end_chars = ".?:"

    i = 0
    length = len(text)

    while i < length:
        line = ""
        # hər bir simvolu oxu
        while i < length and text[i] not in end_chars:
            line += text[i]
            i += 1
        # simvolu da əlavə et əgər mövcuddursa
        if i < length and text[i] in end_chars:
            line += text[i]
            i += 1
        print(line.strip())  # boşluq yox
        print()  # 2-ci new line üçün
