import math
n=int(input('nhap n:'))

def SNT_TT(n):
    print('day snt <={} :'.format(n),end='')
    if n<2:
        print('nothing!')
    else:
        for i in range(2,n+1):
            d=0
            for j in range(2,int(math.sqrt(i)+1)):
                if i%j==0:
                    d=1
                    break
            if d==0:
                print(i,end=' ')

SNT_TT(n)