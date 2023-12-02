# bau cu
import collections

n,m=map(int,input().split())
a=[int(i) for i in input().split()]
res=collections.Counter(a).most_common()
res.sort(key=lambda i:(-i[1],i[0]))
ok=0
for i in range(1,len(res)):
    if res[i][1]<res[0][1]:
        ok=1
        print(res[i][0])
        break

if ok==0: print("NONE")