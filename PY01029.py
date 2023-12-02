# so dao nguyen to cung nhau


import math
for _ in range(int(input())):
    n=input()
    m=int(n[::-1])
    n=int(n)
    if math.gcd(n,m)==1:
        print("YES")
    else: print("NO")