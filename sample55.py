#sample55.py
#coding: utf-8

str = input("文字列を入力")

print("文字列は",str)
print("0番目の文字列は",str[0])
print("文字列を逆順にすると",str[::-1])
print("文字列長は",len(str))

str = input("文字列(英字)を入力")
print("文字列は",str)
print("大文字にすると",str.upper())
print("小文字にすると",str.lower())