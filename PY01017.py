# ma hoa 1

import itertools
for _ in range(int(input())):
    li=list(i for i in input())
    gr= itertools.groupby(li)
    for i,j in gr:
        print(f"{len(list(j))}{i}",end="")
    print()
    