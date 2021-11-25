
list1=[1,2,3,4,5,6,7,8,9]
list2=[1,2,3,4,5]
tonglist=sum(list1)
print('Bai 1: Tong cua list 1: ',tonglist)
t=1
for i in list2:
    t*=i
print('Bai 2: Tich cua list 2: ',t)
listeven=[]
listodd=[]
for i in list1:
    if i%2==0:
        listeven.append(i)
    else:
        listodd.append(i)
print('Bai 3: List moi toan chan: ',listeven)
print('Bai 3: List moi toan le: ',listodd)
list=['Red','Green','White','Black','Pink','Yellow']
new=list[2:4]
print('Bai 4: List moi co 2 phan tu white va black',new)
list3=['zero','three']
list3[1:1]=['one','two']
print('Bai 5: list moi khi them phan tu',list3)
list4=[]
n=int(input('Nhap so luong phan tu trong list: '))
while n>0:
    a=int(input('Nhap gia tri phan tu: '))
    list4.append(a)
    n-=1
print ('Bai 8: List 4 la: ',list4)
print('So lon nhat cua list 4 la: ',max(list4))
print('So nho naht trong list 4 la: ',min(list4))
list5=list4.copy()
print('Bai 10:List duoc copy: ',list5)
