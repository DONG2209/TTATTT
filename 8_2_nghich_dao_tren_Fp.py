import math 

p=int(input('nhap p :'))
a=int(input('nhap a :'))
#  a^-1 mod p
def nghich_dao(a,p):
    x1=1;x2=0
    while(a!=1):
        q=p//a
        r=p-q*a
        x=x2-q*x1
        p=a
        a=r
        x2=x1
        x1=x
    return x1
print('a^-1 mod p =',nghich_dao(a,p))

