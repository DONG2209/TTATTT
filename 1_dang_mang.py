import math
boo=False
try:
    # p=int(input('nhap p :'))
    a=int(input('nhap a :'))
    boo=True
except:
    print('input fail !')

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
    return l
if boo:
    print(('a được biểu diễn qua mảng :'),bieu_dien_mang(a))
