#!/usr/bin/env python3
"""
XML serileştirme ve geri yükleme modülü.
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Bir sözlüğü XML formatına çevirir ve dosyaya kaydeder."""
    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=True)


def deserialize_from_xml(filename):
    """Bir XML dosyasını okur ve Python sözlüğüne dönüştürür."""
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        # XML elemanlarını tekrar sözlüğe dönüştür
        return {child.tag: child.text for child in root}
    except FileNotFoundError:
        return None
