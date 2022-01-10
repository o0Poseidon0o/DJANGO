class Animal:
    def __init__(self, name,age,weight):
        self.name=name
        self.age=age
        self.weight=weight
    def showinfo(self):
        print(self.name)
        print(self.age)
        print(self.weight)

class Mouse(Animal):
    def __init__(self, name,age,weight):
        super(). __init__(name,age,weight)

class DVduoinuoc(Animal):
    def __init__(self, name, age, weight,moitruong):
        super().__init__(name, age, weight)
        self.moitruong=moitruong
    def showinfo(self):
        print(self.name)
        print(self.age)
        print(self.weight)
        print(self.moitruong)
class DVtrencan(DVduoinuoc):
     def __init__(self, name, age, weight,moitruong):
         super().__init__(name, age, weight,moitruong)



chuotjerry=Mouse("jerry",2,0.1)
chuotjerry.showinfo()
Ca=DVduoinuoc("CA",3,1.2,"Duoi nuoc")
Ca.showinfo()
Ga=DVtrencan("Ga",6,3,"tren can")
Ga.showinfo()

class Nguoi:
    def __init__(self, ten,tuoi):
        self.ten=ten
        self.tuoi=tuoi
    def showinfo(self):
        print(self.ten)
        print(self.tuoi)

