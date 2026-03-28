#!/usr/bin/env python3
"""
Temel serileştirme modülü.
"""
import json


def serialize_and_save_to_file(data, filename):
    """Bir Python sözlüğünü JSON dosyasına serileştirir ve kaydeder."""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """JSON dosyasından veriyi yükler ve Python sözlüğüne dönüştürür."""
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
