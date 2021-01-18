# sample69.py
# coding= utf-8

try:
    f = open("sample69.txt","r",encoding='utf-8')

except FileNotFoundError:
    print("ファイルがオープンできない")

else:
    lines = f.readline()
    for line in lines:
        print(line,end="")
    f.close()

finally:
    print("処理終了")
    