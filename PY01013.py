# uoc so chung nguyen to

import math
def nto(m):
    return m>1 and all(m%i!=0 for i in range(2,int(m**0.5)+1))
for _ in range(int(input())):
    a,b=map(int,input().split())
    n=math.gcd(a,b)
    m=sum(int(i) for i in str(n))
    if nto(m):
        print('YES')
    else:
        print('NO')