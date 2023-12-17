# thong ke dich te

n,m=map(int,input().split())
a=[[]]*n
tmp=[[]]*n
for i in range(n):
    a[i]=[int(j) for j in input().split()]
    tmp[i]=[0]*m

res=0
for i in range(n):
    for j in range(m):
        if a[i][j]==-1:
            for x in range(-1,2):
                for y in range(-1,2):
                    if x==0 and y==0: continue
                    if i+x>=0 and i+x<n and j+y>=0 and j+y<m and tmp[i+x][j+y]==0:
                        res+=a[i+x][j+y]
                        tmp[i+x][y+j]=1

print(res)