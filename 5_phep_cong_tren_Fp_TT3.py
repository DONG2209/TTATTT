import math

p=int(input('nhap p :'))
a=int(input('nhap a :'))
b=int(input('nhap b :'))

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
# P=[]
# for i in bieu_dien_mang(a):
#     A.append(i)
# for i in bieu_dien_mang(b):
#     B.append(i)
# for i in bieu_dien_mang(p):
#     P.append(i)

A=bieu_dien_mang(a)
B=bieu_dien_mang(b)
P=bieu_dien_mang(p)

def tinh(x):
    s=0
    for i in range(t):
        s= s+x[i]*pow(2,(t-1-i)*w)
    return s
def tru(A,B): 
    c=[]    
    e=0
    for j in range(t):
        idx=0
        s=A[t-1-j]-B[t-1-j]-e
        if s<0:
            s=s+pow(2,w)
            idx=1
        d=s%(pow(2,w))   
        c.append(d)
        if s>pow(2,w) or idx==1:
            e=1
        else:
            e=0
    c.reverse()
    print('cong tren Fp: c = ',tinh(c))        
    return e,c     
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
    print('cong chinh xac boi (e,C=A+B):({},{})'.format(e,c))
    if e==0:
        print('cong tren Fp :c =',tinh(c))
        return e,c 
    else:
        gtri_c=tinh(c)
        if gtri_c>=p :
            gtri_c-=p 
            print('cong tren Fp :c =',tinh(c))
            return e,bieu_dien_mang(gtri_c)  
        else:
            return tru(c,P)

print('bieu dien p :',P)
print('Tren Fp :(e,c) =',cong(A,B))

          




