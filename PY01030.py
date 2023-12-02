# nguyen to cung nhau

import math
n,k=map(int,input().split())
dem=0
for i in range(10**(k-1),10**k-1):
    if math.gcd(i,n)==1:
        dem+=1
        print(i,end=" ")
        if dem%10==0:
            print()