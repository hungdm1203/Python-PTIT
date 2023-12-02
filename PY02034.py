# dem cac so co hai chu so
import collections

s=input()
a=[]
for i in range(0,len(s),2):
    if int(s[i:i+2])>=10:
        a.append(int(s[i:i+2]))

res=collections.Counter(a)
for i in res:
    print(f"{i} {res[i]}")