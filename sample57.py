#sample57.py
#coding: utf-8

str = input("文字列を入力")
key = input("検索する文字列を入力")

res = str.find(key)

#検索文字列判定
if res != str:
    print(str,"の中に",res,"の位置に",key,"が見つかった")
else:
    print(str,"の中に",key,"が見つからない")

#検索文字列が存在するかどうかだけ確認する
if key in str:
    print(str,"の中に",key,"が見つかった")