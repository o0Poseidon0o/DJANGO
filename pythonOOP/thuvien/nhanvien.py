class Nhanvien:
    def __init__(self,_hoten,_hsl,_giacanh,_thulao,_luongcoban):
        self.hoten=_hoten
        self.hesoluong=_hsl
        self.giacanh=_giacanh
        self.thulao=_thulao
        self.lcb=_luongcoban
    def inthongtin(self):
        print('Họ và tên: ',self.hoten)
        print('Hệ số lương: ',self.hesoluong)
        print('Gia canh: ',self.giacanh)
        print('Thù lao: ',self.thulao)
        print('Lương cơ bản: ',self.lcb)
    def tinhluong(self):
        tntt=self.hesoluong*self.lcb+self.thulao
        tnct=tntt-11000000-(self.giacanh*4400000)
        print('Thu nhập trước thuế: ',tntt)
        print('Thu nhập chịu thuế: ',tnct)
        if(tnct<=5000000):
            a=int(tnct*5/100)
            print('Thu nhập cá nhân Bậc 1:',a)
            print('Thu nhập sau thuế: ',tntt-a)
        elif(tnct>5000000 and tnct<=10000000):
            a=int((tnct*10/100)-250000)
            print('Thu nhập cá nhân Bậc 2: ',a)
            print('Thu nhập sau thuế: ',tntt-a)
        elif(tnct>10000000 and tnct<=18000000):
            a=int((tnct*15/100)-750000)
            print('Thu nhập cá nhân Bậc 3: ',a)
            print('Thu nhập sau thuế: ',tntt-a)
        elif(tnct>18000000 and tnct<=32000000):
            a=int((tnct*20/100)-1650000)
            print('Thu nhập cá nhân Bậc 4: ',a)
            print('Thu nhập sau thuế: ',tntt-a)
        elif(tnct>32000000 and tnct<=52000000):
            a=int((tnct*25/100)-3250000)
            print('Thu nhập cá nhân Bậc 5: ',a)
            print('Thu nhập sau thuế: ',tntt-a)
        elif(tnct>52000000 and tnct<=80000000):
            a=int((tnct*30/100)-5850000)
            print('Thu nhập cá nhân Bậc 6: ',a)
            print('Thu nhập sau thuế: ',tntt-a)
        else:
            a=int((tnct*35/100)-9850000)
            print('Thu nhập cá nhân Bậc 7: ',a)
            print('Thu nhập sau thuế: ',tntt-a)
               
class Nhanvienkd(Nhanvien):
    def __init__(self, _hoten, _hsl, _giacanh, _thulao, _luongcoban,_tylekd):
        super().__init__(_hoten, _hsl, _giacanh, _thulao, _luongcoban)
        self.tlkd=_tylekd

    def nhanvienkd(self):
        tlng=self.lcb*self.tlkd
        print('Thù lao ngoài giờ: ',tlng)
class Nhanviensx(Nhanvien):
    def __init__(self, _hoten, _hsl, _giacanh, _thulao, _luongcoban):
        super().__init__(_hoten, _hsl, _giacanh, _thulao, _luongcoban)

    def __del__(self):
        pass

    