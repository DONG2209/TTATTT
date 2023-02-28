import math

a=int(input('nhap a :'))
b=int(input('nhap b :'))
def ucln(a,b):
    if b==0:
        d=a;x=1;y=0
    else:
        x2=1;x1=0
        y2=0;y1=1
        while(b>0):
            q=a//b
            r=a-q*b
            x=x2-q*x1
            y=y2-q*y1
            a=b;b=r
            x2=x1;x1=x
            y2=y1;y1=y
        d=a
        x=x2 
        y=y2 
        if d==1:
            print('a^-1 mod b:',x)
            print('b^-1 mod a:',y)  
    return d

print('gcd=',ucln(a,b))    



