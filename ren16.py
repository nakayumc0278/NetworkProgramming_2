#ren16.py
#coading: utf-8

import re

ptr = ["Sample.csv", "Sample.exe", "Sample1.py", \
    "Sample2.py", "Sample.txt", "index.html"]
file = []

print("ファイルリストは以下です")
for  i in ptr:
    print(i)

tmp = input("検索する拡張子を入力: ")

for j in str:
    res = j.endswith(tmp)
    if res is True:
        file.append(i)

print("該当するファイルリストは以下です")
for k in file:
    print(k)