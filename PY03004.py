# thong ke tu khac nhau
import re
import collections

a=[]
for _ in range(int(input())):
    a.extend(re.split("[^a-z0-9]",input().lower()))
while "" in a: a.remove("")
res=collections.Counter(a).most_common()
res.sort(key=lambda i: (-i[1],i[0]))
for i in res:print(*i)