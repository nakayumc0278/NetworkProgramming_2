# TEMP FILE !!
# rendb02.py
# coding: utf-8

import sqlite3 as sql

conn = sql.connect("sample.db")

c = conn.cursor()

itr = c.execute("select * from products order by price desc")

for row in itr:
    print(row)

conn.close()