# Bài 13. Viết chương trình kiểm tra tính nguyên tố của một số n nhập vào từ bàn phím theo thuật toán Fermat

import random
n=int(input('nhap n:'))

def binh_phuong(n,a,k):
    b=1
    if k==0:
        return b
    l = []
    while (k>0):
        x = k%2
        l.append(x) 
        k = k//2
    kq = ""
    for i in l:
        kq += str(i)  
    A=a
    if kq[0]=='1':
        b=a
    for i in range(1,len(kq)):
        A=(A**2)%n
        if kq[i]=='1':
            b=(A*b)%n
    return b     

def fermat(n):
    t=50
    for i in range(t):
        # a=random.randint(2,n-1)
        a=2
        r=binh_phuong(n,a,n-1)
        if r!=1:
            return ('Hợp số')        
    return ('Chắc là SNT :))')
print(fermat(n))        