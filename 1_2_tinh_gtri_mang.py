
def tinh():
    w=8
    t=4
    a=[]
    s=0
    print('nhập mảng A :',end='')
    for i in range(t):
        x=int(input())
        a.append(x)
        s= s+a[i]*pow(2,(t-1-i)*w)
    return s
print('a =',tinh())        
    