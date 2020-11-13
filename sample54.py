#sample54.py
#coding: utf-8

import calendar as cl

c = cl.TextCalendar()
yy = int(input("指定年を入力"))
mm = int(input("指定月を入力")) 

c.prmonth(yy,mm)