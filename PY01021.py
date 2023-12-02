# tinh tong cac chu so

import math
for _ in range(int(input())):
    li=list(i for i in input())
    l1=list(i for i in li if i.isalpha())
    l2=list(int(i) for i in li if i.isdigit())
    l1.sort()
    print(''.join(l1)+str(sum(l2)))
