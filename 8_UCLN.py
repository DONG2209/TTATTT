import math

a=int(input('nhap a :'))
b=int(input('nhap b :'))
def ucln(a,b):
    if a==0 or b==0:
        return -1
    else:
        while(b>0):
            q=a//b
            r=a-q*b
            a=b;b=r
    return a

print('gcd=',ucln(a,b))    



