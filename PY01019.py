# khoang cach ki tu

import math
for _ in range(int(input())):
    s=input()
    ss=s[::-1]
    check=1
    for i in range(1,len(s)):
        if abs(ord(s[i])-ord(s[i-1]))!=abs(ord(ss[i])-ord(ss[i-1])):
            check=0
            break
    if check==1:
        print("YES")
    else: print("NO")