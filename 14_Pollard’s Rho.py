import math

a=int(input('nhap a :'))
b=int(input('nhap b :'))

def gcd(a,b):
    while(b>0):
        r=a%b
        a=b
        b=r
    return a
print('d =',gcd(a,b))    