# ren16x.py
# coding: utf-8
import re

str = ["Sample.csv","Sample.exe","Sample1.py",\
    "Sample2.py","Sample1.txt","index.html"]
file = []

print("ファイルは以下の通りです")

for i in str:
    print(i)

suf = input("拡張子を入力してください。")

for i in str:
    res = re.compile(r'.+' + suf +  '$')
    print(res)
    if res is True:
        file.append(i)

print("該当するファイルリストは以下です。")
for j  in file:
    print(j)