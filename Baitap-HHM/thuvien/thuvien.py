import time
def kiemtrasochan(n):
    if n%2==0:
        print('Day la so chan!!!')
    else:
        print('Day la so le!!!')

def kiemtratamgiac(a,b,c):
    if a+b>c and a+c>b and c+b>a:
        print('Day la tam giac!!!!!!')
    else:
        print('Day khong phai la tam giac!!!!!')

def tinhtongdenn(n):
    s=0
    i=1
    while i<=n:
        s=s+i
        i+=i
    print('sum',s)

def tinhtuoi(n):
    x=time.localtime()
    year=x[0]
    print('Số tuổi của bạn',year-n)
def tinhgiaithuadenn(n):
    t=1
    i=1
    while i<=n:
        t=t*i
        i=i+1
    print('giai thua: ',t)
def kiemtranguyenduong(n):
    while n<0:
        print('Nhap lai!!!!')
        break
    n=int(input('Nhap vao so nguyen duong!!!'))

def dthinhchunhat(a,b):
    dt=a*b
    print('dien tich hinh chu nhat: {}'.format(dt))
def dthinhtron(r):
    dt=r*r*3.14
    print('dien tich hinh tron: ', dt)

def giaithua(n): #ham tinh giai thua theo de quy
    if n<0:
        return 0
    else:
        if n==0:
            return 1
        else:
            return n*giaithua(n-1)

def kiemtraconamtrongso(n):
    if n in list(range(3,9)):
        print ('co nam trong khoang nay!!!')
    else:
        print ('khong nam trong khoang nay!!!')