#!/usr/bin/python3
"""
Sınıf örneğini sözlüğe dönüştürme modülü.
"""


def class_to_json(obj):
    """Bir nesnenin sözlük tanımını döndürür."""
    return obj.__dict__
