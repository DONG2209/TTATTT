import math

a=int(input('nhap a :'))
b=int(input('nhap b :'))
def ucln(a,b):
    if b==0:
        d=a
    else:
        while(b>0):
            q=a//b
            r=a-q*b
            a=b;b=r
        d=a
    return d

print('gcd=',ucln(a,b))    



