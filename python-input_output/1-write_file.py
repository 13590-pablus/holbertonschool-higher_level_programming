#!/usr/bin/python3
"""
Dosyaya yazma modülü.
"""


def write_file(filename="", text=""):
    """UTF8 formatında bir dosyaya metin yazar ve karakter sayısını döner."""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
