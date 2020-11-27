#sample63.py
#coding :utf-8

import re

ptr = ["T*","T+","T?","TTTT"]
str = ["X","TT","TTT","TTTT"]

for valueptr in ptr:
    print("------")
    pattern = re.compile(valueptr)
    for valuestr in str:
        res = pattern.search(valuestr)
        if res is not None:
            m  = "〇"
        else:
            m = "×"
        msg = "{パターン}" + valueptr + "{文字列}" + valuestr + "{マッチ}" + m
        print(msg)