#!/usr/bin/python3
"""
Student sınıfı modülü.
"""


class Student:
    """Bir öğrenciyi tanımlayan sınıf."""

    def __init__(self, first_name, last_name, age):
        """Öğrenci niteliklerini başlatır."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Öğrencinin sözlük temsilini döndürür."""
        return self.__dict__
