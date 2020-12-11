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

f = open("sample68x.csv","w",encoding='utf-8')

wt = csv.writer(f)

wt.writerow(["京都","ボールペン",150])
wt.writerows([["広島","万年筆",700],["鹿児島","ノート",120]])

f.close()
