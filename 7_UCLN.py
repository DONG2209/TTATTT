import math

a=int(input('nhap a :'))
b=int(input('nhap b :'))
def ucln(a,b):
    while(b>0):
        r=a%b
        a=b;b=r
    return a
print('gcd=',ucln(a,b))    



