#sample50x.py
#coding: utf-8

class Person:
    def __init__(self, name, nationality, birth, address):
        self.name = name
        self.nationality = nationality
        self.birth = birth
        self.address = address
        
    def show_attribute(self):
        #print('%s %s %s %s' % (self.name, self.nationality, self.birth, self.address))
        print("名前は",self.name,"国は",self.nationality, "誕生日は", self.birth, "住所は",self.address)
p1 = Person("ラザフィ", "まだ出す刈る", "3/25", "opsadpoajpdojap")
p1.show_attribute()