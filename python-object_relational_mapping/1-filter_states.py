#!/usr/bin/python3
"""
Lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Verilənlər bazasına qoşulma
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    # Kursor yaradılır
    cursor = db.cursor()

    # SQL sorğusu: Uzun sətri bölürük ki, pycodestyle xətası verməsin
    query = "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC"
    cursor.execute(query)

    # Nəticələr götürülür
    rows = cursor.fetchall()

    # Çap edilir
    for row in rows:
        print(row)

    # Bağlantılar bağlanır
    cursor.close()
    db.close()
