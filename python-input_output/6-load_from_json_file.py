#!/usr/bin/python3
"""
JSON dosyasından Python nesnesi yükleme modülü.
"""
import json


def load_from_json_file(filename):
    """Bir JSON dosyasından Python nesnesi oluşturur."""
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
