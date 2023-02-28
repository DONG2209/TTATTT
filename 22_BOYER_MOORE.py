# Cài đặt thuật toán tìm kiếm mẫu P trong đoạn văn bản T
# kết quả trả về vị trí xuất hiện của mẫu P theo phương pháp Boyer-Moore

T =input('TEXT T:')
P =input('TEXT P:')
def boyer_moore(T,P):
    i=len(P)-1
    while(i<len(T)):
        j=len(P)-1
        d=1
        while(P[j]==T[i]):
            if j==0:
                return ('Vi tri xh T[{}]'.format(i))
            j-=1
            i-=1
            d+=1
        t,s=0,0
        for x in range(len(P)-d-1,-1,-1):
            t+=1
            if T[i]==P[x]:
                i=i+t
                s=1
                break
        if s==0:
            i=i+len(P)
    return ('P NOT IN T ')
    
print(boyer_moore(T,P))

        
