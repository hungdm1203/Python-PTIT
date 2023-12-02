# tap hop so bang nhau

n,m=map(int,input().split())
a=set(int(i) for i in input().split())
b=set(int(i) for i in input().split())
aa=list(a)
bb=list(b)
aa.sort()
bb.sort()
s=" ".join([str(i) for i in aa])
ss=" ".join([str(i) for i in bb])
if s==ss: print("YES")
else: print("NO")