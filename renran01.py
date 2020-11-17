#renran01.py
#coding: utf-8

import random as rd

#アルファベット配置
alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "h", "j", "k", "l", "m", \
    "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

value = rd.choice(alpha)

#-print(value)

while True:
    inp = input("小文字の英字を１文字指定")
    
    if value != inp:
        print("NG")
    else:
        print("OK")
        break