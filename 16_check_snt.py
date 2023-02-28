# Bài 12. Viết chương trình kiểm tra tính nguyên tố của một số n nhập vào từ bàn phím theo cách thông thường.
import math
n=int(input('nhap n:'))

def check_snt(n):
    if n<2:
        return False
    else:
        for i in range(2,int(math.sqrt(n)+1)):
            if n%i ==0:
                return False
        return True

print(check_snt(n))        