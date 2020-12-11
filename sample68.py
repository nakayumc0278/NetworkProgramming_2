# sample68.py
# coding: utf-8

import csv

f = open("sample68.csv","r",encoding='utf-8')

rd = csv.reader(f)

for row in rd:
    for col in row:
        print(col,end=",")
    print()

f.close()