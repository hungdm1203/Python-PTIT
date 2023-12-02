# chia het cho k

a,k,n=map(int,input().split())
bmax=int(n/k)*k-a
bmin=(int(a/k)+1)*k-a
if bmax>=bmin:
    for i in range(bmin,bmax+1,k):
        print(i,end=" ")
else: print(-1)