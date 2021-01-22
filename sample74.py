# sample74.py
# coding: utf-8

import sqlite3 as sql

conn = sql.connect("sample.db")

c = conn.cursor()

itr = c.execute("select * from products where price >= 100000")

for row in itr:
    print(row)

conn.close()