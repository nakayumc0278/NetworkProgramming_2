# rendb02.py
# coding: utf-8

import sqlite3 as sql

conn = sql.connect("sampleren.db")

c = conn.cursor()

itr = c.execute("select * from sales where sales >= 50000 order by sales")

for row in itr:
    print(row)

conn.close()