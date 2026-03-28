#!/usr/bin/python3
"""
Dosya okuma modülü.
"""


def read_file(filename=""):
    """UTF8 formatındaki bir metin dosyasını okur ve yazdırır."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
