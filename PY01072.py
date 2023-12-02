# bai toan to hop


import itertools
n,k=map(int,input().split())
s=set(int(i) for i in input().split())
li=list(s)
li.sort()
a=list(itertools.combinations(li,k))
for i in a:
    print(*i)