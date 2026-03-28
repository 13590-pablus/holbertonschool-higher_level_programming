#!/usr/bin/python3
"""
Nesneyi JSON formatında dosyaya kaydetme modülü.
"""
import json


def save_to_json_file(my_obj, filename):
    """Bir nesneyi JSON temsiliyle bir metin dosyasına yazar."""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
