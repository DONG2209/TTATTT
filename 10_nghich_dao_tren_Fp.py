import math 
p=int(input('nhap p :'))
a=int(input('nhap a :'))
#  a^-1 mod p
def nghich_dao():
    u=a;v=p
    x1=1;x2=0
    while(u!=1):
        q=v//u
        r=v-q*u
        x=x2-q*x1
        v=u
        u=r
        x2=x1
        x1=x
    return(x1%p)
print('a^-1 mod p =',nghich_dao())