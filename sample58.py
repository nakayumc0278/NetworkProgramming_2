#sample58.py
#coding: utf-8

str1 = input("文字列を入力")
old = input("置換される文字列を入力")
new = input("置換する文字列を入力")

if old in str1:
    str2 = str1.replace(old,new)
    print(str2,"に置き換えました")
else:
    print(str + "の中に" + old + "が見つかりません")