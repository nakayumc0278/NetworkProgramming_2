# sample73.py
# coding: utf-8

import sqlite3 as sql

conn = sql.connect("sample.db")

c = conn.cursor()

c.execute("drop table if exists products")

c.execute("create table products(name   char(30),price  int)")
c.execute("insert into products values('空気清浄機',20000)")
c.execute("insert into products values('冷蔵庫',170000)")
c.execute("insert into products values('エアコン',99000)")
c.execute("insert into products values('液晶テレビ',120000)")
c.execute("insert into products values('ノートパソコン',135000)")

conn.commit()

itr = c.execute("select * from products")

for row in itr:
    print(row)

conn.close()