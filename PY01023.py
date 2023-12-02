# phan tich thua so nguyen to


import math
import itertools
def ptich(n):
    i=2
    a=[]
    while i<=int(n**0.5)+1:
        if n%i==0:
            a.append(i)
            n=n/i
        else: i=i+1
    a.append(int(n))
    return a

for _ in range(int(input())):
    n=int(input())
    li=ptich(n)
    a=itertools.groupby(li)
    print("1",end="")
    for i,j in a:
        print(f" * {i}^{len(list(j))}",end="")
    print()  