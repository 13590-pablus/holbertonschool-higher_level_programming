#!/usr/bin/env python3
"""
Pickle kullanarak özel nesne serileştirme modülü.
"""
import pickle


class CustomObject:
    """Özel bir nesne tanımlayan sınıf."""

    def __init__(self, name, age, is_student):
        """Özellikleri başlatır."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Nesne niteliklerini ekrana yazdırır."""
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """Mevcut nesneyi bir dosyaya serileştirir (pickle)."""
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Bir dosyadan nesneyi geri yükler (unpickle)."""
        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except (FileNotFoundError, EOFError, pickle.UnpicklingError, Exception):
            return None
