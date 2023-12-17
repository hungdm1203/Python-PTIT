# training he thong a.i

import collections

for _ in range(int(input())):
    n=int(input())
    t=float(input())
    a=[float(i) for i in input().split()]
    a=collections.Counter(a).most_common()
    a=[[i[0],i[1]] for i in a]
    a.sort(key=lambda i:(i[0]))
    while len(a)>1:
        tmp=a[1][0]-a[0][0]
        if t>tmp*a[0][1]:
            a[1][1]+=a[0][1]
            t=t-tmp*a[0][1]
            a.pop(0)
        else: break
    a[0][0]+=t/a[0][1]
    mul=1
    for i in a:
        mul=mul*(i[0]**i[1])
    mul=min(1,mul)
    print(f"{mul:.6f}")