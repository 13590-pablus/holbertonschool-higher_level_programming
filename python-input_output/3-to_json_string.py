#!/usr/bin/python3
"""
JSON string dönüştürme modülü.
"""
import json


def to_json_string(my_obj):
    """Bir nesnenin JSON temsilini (string olarak) döner."""
    return json.dumps(my_obj)
