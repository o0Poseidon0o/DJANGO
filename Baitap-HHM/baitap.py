import time
a=int(input('Nhap vao mot so nguyen: '))
if a%2==0:
    print('Day la so chan!!!')
else:
    print('Day la so le!!!!')

a=int(input('Nhap vao canh a: '))
b=int(input('Nhap vao canh b: '))
c=int(input('Nhap vao canh c: '))
if a+b>c and a+c>b and c+b>a:
    print('Day la tam giac!!!!!!')
else:
    print('Day khong phai la tam giac!!!!!')

a=int(input('Nhap vao nam sinh: '))
x=time.localtime()
year=x[0]
print('Số tuổi của bạn',year-a)