# sap xep day so

for _ in range(int(input())):
    n,m=map(int,input().split())
    a=list(int(i) for i in input().split())
    ma=max(a)
    id=a.index(ma)
    a.insert(id,m)
    b=list(i for i in a if i<0)
    print(*b,end=" ")
    for i in a:
        if i>=0: print(i,end=" ")
    print()
    