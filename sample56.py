#sample56.py
#coding: utf-8

print("{0}は{1}{2}です".format("今日","よい","天気"))
print("{key1}支店の{key2}です\n".format(key1="東京",key2="売上"))

word0 = input("1つ目の単語を入力")
word1 = input("2つ目の単語を入力")
word2 = input("3つ目の単語を入力")

print("{0}は{1}{2}です".format(word0,word1,word2))
num0 = int(input("個数を入力"))
num1 = int(input("金額を入力"))

print("{0:<}個{1:>10,}円".format(num0,num1))