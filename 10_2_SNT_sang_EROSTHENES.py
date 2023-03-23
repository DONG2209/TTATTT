import time
n=int(input('nhap n:'))

def sang_EROSTHENES(n):
    print('day snt <={} :'.format(n),end='')
    if n<2:
        print('nothing!')
    else:
        l=[True]*(n+1)
        for i in range(2,n+1):
            if l[i]==True:
                for j in range(i*2,n+1,i):
                    l[j]=False
                print(i,end=' ')
                
start_time=time.time()                  
sang_EROSTHENES(n)       
end_time=time.time()
print('\ntime =',end_time-start_time)
