# thong ke tu khac nhau khong chua chu so

import re
import collections

a=[]
for _ in range(int(input())):
    a.extend(re.split("[^a-z]",input().lower()))
while "" in a: a.remove("")
res=collections.Counter(a).most_common()
res.sort(key=lambda i: (-i[1],i[0]))

for i in res: print(*i)