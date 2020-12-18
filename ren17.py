# ren17.py
# coding: utf-8


def dict_info(dict_tbl, key):
    return dict_tbl[key]


name_age = {"tanaka": 33, "satou": 23, "suzuki": 29}

try:
    print(dict_info(name_age, "yamada"))
    # print(dict_info(name_age, "satou"))

except KeyError:
    print("Key is not found")