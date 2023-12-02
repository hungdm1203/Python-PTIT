# bien doi ve ma tran vuong

n,m=map(int,input().split())
a=[]
for i in range(n):
    li=[int(i) for i in input().split()]
    a.append(li)


res=[]
if n>m:
    for i in range(n):
        if len(res)+n-i==m:
            res.append(a[i])
            continue
        if i%2!=0:
            res.append(a[i])
elif n<m:
    for i in a:
        tmp=[]
        for j in range(m):
            if len(tmp)+m-j==n:
                tmp.append(i[j])
                continue
            if j%2==0: tmp.append(i[j])
        res.append(tmp)
else: res=a
for i in res:
    print(*i)