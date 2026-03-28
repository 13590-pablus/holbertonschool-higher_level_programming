#!/usr/bin/python3
"""
Komut satırı argümanlarını bir listeye ekleyen ve JSON dosyasına kaydeden script.
"""
import sys
import os

# Önceki görevlerdeki fonksiyonları import ediyoruz
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

# Eğer dosya varsa içindekileri yükle, yoksa boş bir liste oluştur
if os.path.exists(filename):
    items = load_from_json_file(filename)
else:
    items = []

# Komut satırından gelen argümanları listeye ekle (script adını atla: [1:])
items.extend(sys.argv[1:])

# Güncellenmiş listeyi dosyaya geri kaydet
save_to_json_file(items, filename)
