# nguong toi thieu

import collections

s=input()
k=int(input())
ok=0
a=[]
for i in range(0,len(s),2):
    if int(s[i:i+2])>=10:
        a.append(int(s[i:i+2]))
a.sort()
res=collections.Counter(a)
for i in res:
    if res[i]>=k:
        ok=1
        print(f"{i} {res[i]}")

if ok==0: print("NOT FOUND")