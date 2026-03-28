#!/usr/bin/env python3
"""
CSV verilerini JSON formatına dönüştürme modülü.
"""
import csv
import json


def convert_csv_to_json(csv_filename):
    """CSV dosyasını okur ve içeriğini data.json olarak kaydeder."""
    try:
        data = []
        with open(csv_filename, 'r', encoding='utf-8') as csv_f:
            # DictReader her satırı bir sözlük olarak okur
            reader = csv.DictReader(csv_f)
            for row in reader:
                data.append(row)

        with open('data.json', 'w', encoding='utf-8') as json_f:
            # Listeyi JSON formatında dosyaya yazar
            json.dump(data, json_f)

        return True
    except FileNotFoundError:
        return False
    except Exception:
        return False
