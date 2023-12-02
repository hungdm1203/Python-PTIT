# so may man trong ma tran



n,m=map(int,input().split())
a=[]
ma=0
mi=10001
for _ in range(n):
    li=[int(i) for i in input().split()]
    a.append(li)
    mi=min(mi,min(li))
    ma=max(ma,max(li))
ok=0
for i in a:
    if ma-mi in i: ok=1

if ok==0:
    print("NOT FOUND")
else:
    print(ma-mi)
    for i in range(n):
        for j in range(m):
            if a[i][j]==ma-mi:
                print(f"Vi tri [{i}][{j}]")