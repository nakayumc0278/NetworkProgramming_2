import random as rd

#1未満のfloat型の乱数を取得
num = rd.random()
print("random =", num)

#第１引数と第２引数の範囲内でfloat型の値を返す
num = rd.uniform(1.0,10.0)
print("uniform =", num)

#int型の値を返す
num = rd.randint(1,30)
print("randint =", num)

#リストや文字列など中身取得
mylist = ["apple", "banana", "melon", "strawberry", "peach", "lemon"]
print("mylist =",rd.choice(mylist))

#配列の中身をシャッフルする
print("現在のデータ =",mylist)
rd.shuffle(mylist)
print("変更後のデータ =",mylist)

