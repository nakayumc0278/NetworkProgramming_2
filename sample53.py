#sample53.py
#coding: utf-8

import myclass

pr = myclass.Costomer("鈴木",23,"alx@sample.co.jp","xxx-xxxx-xxxx")
nm = pr.getName()
ag = pr.getAge()
ad = pr.getAdr()
tl = pr.getTel()

print(nm,"さんは",ag,"才です")
print("アドレスは",ad,"電話番号は",tl)
