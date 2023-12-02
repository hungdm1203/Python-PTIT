# gui thong bao

for _ in range(int(input())):
    a=list(i for i in input().split())
    s=0
    id=0
    for i in range(len(a)):
        if s+len(a[i])+1>100: 
            id=i
            break
        s=s+len(a[i])+1

    if id!=0: print(*a[:id])
    else: print(*a)

