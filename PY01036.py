# tinh tong phan thuc


import math
for _ in range(int(input())):
    n=int(input())
    if n%2==0:
        li=list(float(1/i) for i in range(2,n+1,2))
        print(f"{sum(li):.6f}")
    else:
        li=list(float(1/i) for i in range(1,n+1,2))
        print(f"{sum(li):.6f}")