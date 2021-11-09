#Xay dung class
from typing import Match


import math
class Triangle:
    def __init__(self,_a,_b,_c):
        self.a=_a
        self.b=_b
        self.c=_c
    def tinh_chu_vi(self):
        cv=self.a +self.b+self.c
        return cv
    def tinh_dien_tich(self):
        nua_cv=self.tinh_chu_vi()/2
        dt=math.sqrt(nua_cv*(nua_cv-self.a)*(nua_cv - self.b)*(nua_cv - self.c))
        return dt
    def __str__(self):
        chuoi_kq= 'Chu chi tam giac: ' + str(self.tinh_chu_vi())
        chuoi_kq += '\n Dien tich tam giac ' + str(self.tinh_dien_tich)
        return chuoi_kq
    def __del__ (self):
        pass
# Nhap du lieu dau vao
canh_1= int(input('Nhap canh 1: '))
canh_2= int (input('Nhap canh 2: '))
canh_3=int(input('Nhap canh 3: '))

if canh_1 + canh_2 >canh_3 and canh_2+canh_3 > canh_1 and canh_1 + canh_3>canh_2:
     tg1= Triangle(canh_1,canh_2,canh_3)
     print(tg1)
     print(tg1.tinh_chu_vi())
     print(tg1.tinh_dien_tich())

     print(getattr(tg1, 'a'))
     print(hasattr(tg1, 'a'))
else:
    print('khong phai tam giac')