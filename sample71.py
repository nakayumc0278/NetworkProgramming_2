# sample71.py
# coding: utf-8

import os
import os.path

curdir = os.listdir(".")

for name in curdir:
    print(os.path.abspath(name), end="")

    if os.path.isfile(name):
        print("ファイルです")
    else:
        print("ディレクトリです")
print()