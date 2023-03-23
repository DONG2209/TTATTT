# Cài đặt thuật toán tìm kiếm mẫu P trong đoạn văn bản T
# kết quả trả về vị trí xuất hiện của mẫu P theo phương pháp vét cạn (không sử dụng hàm có sẵn)

T =input('TEXT T:')
P =input('TEXT P:')
def vet_can(T,P):
    for i in range(len(T)-len(P)+1):
        j=0
        while(P[j]==T[i]):
            j+=1
            i+=1
            if j==len(P) :
                return ('T[{}]'.format(i-j))
    return (' P Not IN T ')
print('Vi tri xh :',vet_can(T,P))
