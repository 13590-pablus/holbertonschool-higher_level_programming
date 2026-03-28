#!/usr/bin/python3
"""
Pascal Üçgeni modülü.
"""


def pascal_triangle(n):
    """n boyutunda Pascal Üçgeni temsil eden liste listesi döner."""
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        prev_row = triangle[i - 1]
        
        # İç kısımdaki sayıları hesapla (üstteki iki sayının toplamı)
        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])
            
        row.append(1)
        triangle.append(row)

    return triangle
