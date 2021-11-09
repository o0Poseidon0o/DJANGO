class ConNguoi:
    def __init__(self, ho_ten, dia_chi,_gioi_tinh, ngay_sinh):
        self.ho_ten = ho_ten
        self.dia_chi = dia_chi
        self.gioi_tinh= _gioi_tinh
        self.ngay_sinh = ngay_sinh
    
    def in_thong_tin(self):
        print(self.ho_ten)
        print(self.dia_chi)
        print(self.gioi_tinh)
        print(self.ngay_sinh)

    def __del__(self):
        pass

class Nhanvien(ConNguoi):
    def __init__(self, ho_ten, dia_chi, _gioi_tinh, ngay_sinh, msnv, luong):
        super().__init__(ho_ten, dia_chi, _gioi_tinh, ngay_sinh)
        self.msnv=msnv
        self.luong=luong
    def in_thong_tin(self):
        print(self.ho_ten)
        print(self.dia_chi)
        print(self.gioi_tinh)
        print(self.ngay_sinh)
        print(self.msnv)
        print(self.luong)
    def __del__(self):
        pass

cn=ConNguoi('a','12','45','34')
cn.in_thong_tin()

nv=Nhanvien('34','5345','3535','3535','3535','3535')
nv.in_thong_tin()

print(issubclass(Nhanvien,ConNguoi)) #kiem tra moi quan he class
print(isinstance(nv,ConNguoi)) #Bien nay thuoc class con nguoi khong

