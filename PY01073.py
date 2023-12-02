# hoan vi ky tu


import itertools
li=list(i for i in input())
a=itertools.permutations(li)
for i in a:
    print(''.join(i))