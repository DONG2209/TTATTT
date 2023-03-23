# a^k mod n

n=int(input('nhap n:'))
a=int(input('nhap a:'))
k=int(input('nhap k:'))

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
print('kq =',binh_phuong(n,a,k))

    

    



