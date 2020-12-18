# ren19.py
# coding: utf-8

import os
import os.path
import datetime

curdir = os.listdir(".")

print("名前\t\t 最終アクセス時刻")

for name in curdir:
    print(
        os.path.basename(name),
        "\t",
        datetime.datetime.fromtimestamp(os.path.getmtime(name)),
    )
