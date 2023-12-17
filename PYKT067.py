# hoan vi nguoc

import itertools

for _ in range(int(input())):
    a=[str(i) for i in range(1,1+int(input()))]
    res=list(itertools.permutations(a,len(a)))
    print(len(res))
    for i in range(len(res)-1,-1,-1):
        print(''.join(res[i]),end=" ")
    print()