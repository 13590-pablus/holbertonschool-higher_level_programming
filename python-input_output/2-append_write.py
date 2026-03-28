#!/usr/bin/python3
"""
Dosyanın sonuna ekleme yapma modülü.
"""


def append_write(filename="", text=""):
    """UTF8 formatında dosyanın sonuna metin ekler ve eklenen karakter sayısını döner."""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
