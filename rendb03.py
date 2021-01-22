# rendb03.py
# coding: utf-8

import sqlite3 as sql

conn = sql.connect("sample.db")

c = conn.cursor()

itr = c.execute("select * from products where name = '液晶テレビ' OR price <= 100000")

for row in itr:
    print(row)

conn.close()