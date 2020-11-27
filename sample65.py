#sample65.py
#coding: utf-8

import re

ptr = "\.(csv|html|py)$"
str = ["Sample.csv", "Sample.exe", "Test.py", "index.html"]

pattern = re.compile(ptr)
for valuestr in str:
    res = pattern.sub(".txt",valuestr)
    msg = "(変換前)" + valuestr + "(変換後)" + res
    print(msg)
