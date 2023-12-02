# xau thang bang

import math
for _ in range(int(input())):
    s=input()
    ss=s[::-1]
    if all(abs(ord(s[i])-ord(s[i-1]))==abs(ord(ss[i])-ord(ss[i-1])) for i in range(1,len(s))):
        print("YES")
    else: print("NO")
