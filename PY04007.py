# lop matrix-1


for _ in range(int(input())):
    n,m=map(int,input().split())
    a=[]
    for i in range(n):
        a.append(list(int(j) for j in input().split()))

    b=[]
    for i in range(m):
        tmp=[]
        for j in range(n):
            tmp.append(a[j][i])
        b.append(tmp)

    res=[]
    for i in range(n):
        tmp=[]
        for j in range(n):
            x=0
            for k in range(m): x+=a[i][k]*b[k][j]
            tmp.append(x)
        res.append(tmp)
    
    for i in res: print(*i)