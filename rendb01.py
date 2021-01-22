# rendb01.py
# coding: utf-8

import sqlite3 as sql

conn = sql.connect("sampleren.db")

c = conn.cursor()

c.execute("drop table if exists sales") 

c.execute("create table sales (product char(20),quantity int, sales int)")
c.execute("insert into sales values('みかん', 100, 45000)")
c.execute("insert into sales values('りんご', 80, 80000)")
c.execute("insert into sales values('バナナ', 150, 30000)")
c.execute("insert into sales values('いちご', 200, 35000)")
c.execute("insert into sales values('スイカ', 300, 50000)")

conn.commit()

itr = c.execute("select * from sales")

for row in itr:
    print(row)

conn.close()