#sample55.py
#coding: utf-8

str = input("文字列を入力")

print("文字列は",str)
print("0番目の文字列は",str[0])
print("文字列を逆順にすると",str[::-1])
print("文字列長は",len(str),"\n")

str = input("文字列(英字)を入力")
print("\n文字列は\t",str)
print("大文字にすると\t",str.upper())
print("小文字にすると\t",str.lower())
print("大小変換\t\t",str.swapcase())
print("タイトルを取得\t",str.title())
# print("中央揃え取得\t",str.center())
# print("左寄せ取得\t",str.ljust())
# print("右寄せ取得\t",str.rjust())
print("空白除去\t",str.strip())
print("先頭空白除去\t",str.lstrip())
print("末尾空白除去\t",str.rstrip())
