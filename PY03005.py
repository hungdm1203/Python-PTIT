# thong ke tu khac nhau thoe nguong k

import re
import collections

a=[]
n,k=map(int,(input().split()))
for _ in range(n):
    a.extend(re.split("[^a-z0-9]",input().lower()))

while "" in a: a.remove("")
res=collections.Counter(a).most_common()
res.sort(key=lambda i:(-i[1],i[0]))
for i in res: 
    if i[1]>=k: print(*i)
    else: break

