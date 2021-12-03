from thuvien import thuvien

a=int(input('Chieu dai: '))
b=int(input('chieu rong: '))
thuvien.dthinhchunhat(a,b)

r=int(input('Ban kinh cua hinh tron: '))
thuvien.dthinhtron(r)

n=int(input('Nhap n: '))
print('Giai thua cua so n: ',thuvien.giaithua(n))

n=int(input('Nhap vao so bat ki: '))
thuvien.kiemtraconamtrongso(n)


a=input('Nhap 1 chuoi vao: ')
b=a.split(" ")
for i in b:
    if i==str.isupper():
        i+=1
    else:
        i+=1
print(i)