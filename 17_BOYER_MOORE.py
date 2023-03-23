# Cài đặt thuật toán tìm kiếm mẫu P trong đoạn văn bản T
# kết quả trả về vị trí xuất hiện của mẫu P theo phương pháp Boyer-Moore

T =input('TEXT T:')
P =input('TEXT P:')

def last_occurrence(P):
    L=[-1]*256  # Khởi tạo mảng last với giá trị -1 cho mỗi ký tự ASCII
    for i ,char in enumerate(P):
        L[ord(char)]=i  # Lưu vị trí xuất hiện cuối cùng của ký tự trong P
    return L

# c2 không sử dụng enumerate
def last_occurrence(P):
    last = [-1] * 256
    for i in range(len(P)):
        last[ord(P[i])] = i
    return last
def boyer_moore(T,P):
    L=last_occurrence(P)
    m=len(P)
    n=len(T)
    i=m-1
    while(i<n):
        j=m-1
        while(P[j]==T[i]):
            if j==0:
                return ('Vi tri xh T[{}]'.format(i))
            j-=1
            i-=1
        i=i+m-min(j,1+L[ord(T[i])])
    return ('P NOT IN T ')       
print(boyer_moore(T,P))


# T =input('TEXT T:')
# P =input('TEXT P:')
# def boyer_moore(T,P):
#     i=len(P)-1
#     while(i<len(T)):
#         j=len(P)-1
#         d=0
#         while(P[j]==T[i]):
#             if j==0:
#                 return ('Vi tri xh T[{}]'.format(i))
#             j-=1
#             i-=1
#             d+=1
#         t,s=1,0
#         for x in range(len(P)-d-2,-1,-1):
#             if T[i]==P[x]:
#                 i=i+t
#                 s=1
#                 break
#             t+=1
#         if s==0:
#             i=i+len(P)
#     return ('P NOT IN T ')
    
# print(boyer_moore(T,P))

        
