# tong fibonacci


fib=[0,1]
for i in range(2,93):
    fib.append((fib[i-1]+fib[i-2])%(10**9+7))


n,m=map(int,input().split())
a=[int(i) for i in input().split()]
for _ in range(m):
    li=[int(i) for i in input().split()]
    if li[0]==1:
        for i in range(li[1],li[2]+1):
            a[i-1]+=li[3]
    else:
        res=0
        for i in range(li[1],li[2]+1):
            res=(res+fib[a[i-1]])%(10**9+7)
        print(res)