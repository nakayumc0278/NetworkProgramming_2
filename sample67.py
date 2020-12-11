# sample67.py
# coding: utf-8

f = open("sample66.txt","r",encoding='utf-8')

lines = f.readlines()

for line in lines:
    print(line,end="")

f.close()