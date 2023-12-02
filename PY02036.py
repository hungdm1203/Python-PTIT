# liet ke cap so nguyen to cung nhau

import math

n=int(input())
li=list(int(i) for i in input().split())
li.sort()
for i in range(len(li)-1):
    for j in range(i+1,len(li)):
        if math.gcd(li[i],li[j])==1:
            print(f"{li[i]} {li[j]}")