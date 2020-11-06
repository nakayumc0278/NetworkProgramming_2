#sample50.py
#coding: utf-8

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

pr = Person("田中",25)
n = pr.getName()
a = pr.getAge()

print(n,"さんは",a,"才です")