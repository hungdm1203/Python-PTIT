# dat ten


import itertools
a,b=map(int,input().split())
s=set(i for i in input().split())
li=list(s)
li.sort()
a=list(itertools.combinations(li,b))
for i in a:
    print(" ".join(i))