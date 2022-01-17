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

class Hinhchunhat:
    def __init__(self, a,b):
        self.a=a
        self.b=b
    def chuvi(self):
        cv=(self.a+self.b)*2
        return cv
    def dientich(self):
        dt=self.a*self.b
        return dt
    def showinfo(self):
        print(self.a)
        print(self.b)
hinhchunhat=Hinhchunhat(5,6)
hinhchunhat.showinfo()
print(hinhchunhat.chuvi())
print(hinhchunhat.dientich())

a=int(input('nhap chieu dai: '))
b=int(input('nhap chieu rong: '))
hinhchunhat=Hinhchunhat(a,b)
print(hinhchunhat.chuvi())
print(hinhchunhat.dientich())

class Hocvien:
    def __init__(self,mahocvien,hoten,Toan,Ly,Hoa):
        self.mhv=mahocvien
        self.hoten=hoten
        self.Toan=Toan
        self.Ly=Ly
        self.Hoa=Hoa
    def diemtb(self):
        dtb=(self.Toan+self.Ly+self.Hoa)/3
        return dtb
    def showinfo(self):
        print(self.mhv)
        print(self.hoten)
        print(self.Toan)
        print(self.Ly)
        print(self.Hoa)
class hv1(Hocvien):
    def __init__(self, mahocvien, hoten, Toan, Ly, Hoa):
        super().__init__(mahocvien, hoten, Toan, Ly, Hoa)


hocvien=Hocvien(456,"Nguyen Van A",6,7,8)
hocvien.showinfo()
print(hocvien.diemtb())



