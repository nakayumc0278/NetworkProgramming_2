#sample49v2.py
#coding: utf-8

class Person:
    def getName(self):
        return self.name

    def getAge(self):
        return self.age

pr1 = Person()
pr1.name = "田中"
pr1.age = 25
n1 = pr1.getName()
a1 = pr1.getAge()

pr2 = Person()
pr2.name = "佐藤"
pr2.age = 30
n2 = pr2.getName()
a2 = pr2.getAge()

print(n1,"さんは",a1,"才です")
print(n2,"さんは",a2,"才です")