# ren18.py
# coding: utf-8

import os
import os.path

curdir = os.listdir(".")

for name in curdir:
    print(os.path.basename(name), "\t", os.path.getsize(name), "バイト")

print()