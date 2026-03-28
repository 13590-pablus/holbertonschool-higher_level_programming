#!/usr/bin/python3
"""
Student sınıfı modülü - Reload özellikli.
"""


class Student:
    """Bir öğrenciyi tanımlayan sınıf."""

    def __init__(self, first_name, last_name, age):
        """Öğrenci niteliklerini başlatır."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Öğrencinin sözlük temsilini döndürür."""
        if isinstance(attrs, list) and all(isinstance(s, str) for s in attrs):
            res = {}
            for a in attrs:
                if hasattr(self, a):
                    res[a] = getattr(self, a)
            return res
        return self.__dict__

    def reload_from_json(self, json):
        """Nesnenin tüm niteliklerini verilen sözlükle günceller."""
        for key, value in json.items():
            setattr(self, key, value)
