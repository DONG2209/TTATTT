import math
import array as arr

a=int(input('nhap a :'))
b=int(input('nhap b :'))

p=2147483647
w=8
m=round(math.log2(p),0)
t=int(round((m/w),0))

def bieu_dien_mang(a):
    l=[]
    d=0
    for i in range(t): 
        s=(pow(2,(t-1-i)*w))
        x=(a-d)//s
        l.append(x)
        d+=x*s
    return(l)

# A=[]
# B=[]
# for i in bieu_dien_mang(a):
#     A.append(i)
# for i in bieu_dien_mang(b):
#     B.append(i)

A=bieu_dien_mang(a)
B=bieu_dien_mang(b)

def cong(A,B): 
    c=[]    
    e=0
    for j in range(t):
        s=A[t-1-j]+B[t-1-j]+e
        d=s%(pow(2,w))
        c.append(d)
        if s< pow(2,w) :
            e=0
        else:
            e=1
    c.reverse()        
    return e,c 
print('(e,C) = ',cong(A,B))             




