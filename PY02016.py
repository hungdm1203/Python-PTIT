#  xuat hien nhieu lan nhat

import collections


for _ in range(int(input())):
    n=int(input())
    li=list(int(i) for i in input().split())
    a=collections.Counter(li)
    li.clear()
    dem= max(a.values())
    if dem>int(n/2):
        for i,j in a.items():
            if j==dem:
                li.append(i)
        print(min(li))
    else:
        print("NO")