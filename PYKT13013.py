# tinh tong tren ma tran

mod=1000000007
n,m,k=map(int,input().split())
a=[]
for i in range(n):
    tmp=[j for j in range(i*m+1,(i+1)*m+1)]
    a.append(tmp)

while k>0:
    k-=1
    x,y,z=input().split()
    if x=='R':
        for i in range(m):
            a[int(y)-1][i]*=int(z)
            a[int(y)-1][i]%=mod
    else:
        for i in range(n):
            a[i][int(y)-1]*=int(z)
            a[i][int(y)-1]%=mod

res=0
for i in a: 
    for j in j:
        res=(res+j)%mod
print(res)