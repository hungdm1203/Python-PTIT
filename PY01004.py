# nguyen to

import math
def nto(n):
    return n>1 and all(n%i!=0 for i in range(2,int(n**0.5)+1))
for _ in range(int(input())):
    n=int(input())
    dem=0
    for i in range(1,n):
        if math.gcd(i,n)==1:
            dem+=1
    if nto(dem):
        print('YES')
    else: print('NO')