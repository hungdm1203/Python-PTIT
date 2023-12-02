# kiem tra nguyen to

import math
def nto(n):
    return n>=2 and all(n%i!=0 for i in range(2,int(n**0.5)+1))


for _ in range(int(input())):
    s=input()
    n=int(s[-4::1])
    if nto(n):
        print("YES")
    else: print("NO")