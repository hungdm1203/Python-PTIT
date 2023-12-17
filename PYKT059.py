# thanh phan lien thong

def dfs(s):
    vs[s]=1
    for i in a[s]:
        if vs[i]==0: dfs(i)


n,m,s=map(int,input().split())
a={}
vs=[0]*(n+1)
for i in range(1,n+1):
    a[i]=[]

for _ in range(m):
    i,j=map(int,input().split())
    a[i].append(j)
    a[j].append(i)

dfs(s)
for i in range(1,len(vs)):
    if vs[i]==0: print(i)