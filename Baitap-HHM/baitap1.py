n = int(input("Enter 3 digit number: "))                  
s = 0                                                     
k = n                                                     
while k>0:                                                
    d = k%10                                              
    s = s + (d**3)                                        
    k = k//10                                             
if n == s:                                                
    print('{} is an Armstrong number'.format(n))          
else:                                                       
    print('{} is not an Armstrong number'.format(n))

print("Nhập vào số N lớn hơn 0: ")
 
n = int(input())
tong = 0
 
for i in range(1, n):
    if (n % i == 0):
        tong += i
 
if (tong == n):
    print(n, " là số hoàn hảo")
else:
    print(n, " không phải là số hoàn hảo")
