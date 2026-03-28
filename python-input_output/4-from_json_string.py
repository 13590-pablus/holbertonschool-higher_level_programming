#!/usr/bin/python3
"""
JSON string'inden Python nesnesine dönüşüm modülü.
"""
import json


def from_json_string(my_str):
    """Bir JSON string'ini Python veri yapısına (nesneye) dönüştürür."""
    return json.loads(my_str)
