#sample49.py
#coding: utf-8

class Person:
    def getName(self):
        return self.name

    def getAge(self):
        return self.age

pr = Person()

pr.name = "田中"
pr.age = 25

n = pr.getName()
a = pr.getAge()

print(n,"さんは",a,"才です")