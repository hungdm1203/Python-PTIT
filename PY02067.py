# day so tuong thich

n=int(input())
a=[int(i) for i in input().split()]

mi=0
s=10**8
for i in range(1,min(a)):
    b=[]
    ok=1
    for j in range(len(a)):
        b.append(a[j]//(i+1)+1)
    for j in range(len(b)-1):
        if a[j]//b[j]!=a[j+1]//b[j+1]:
            ok=0
            break
    if ok==1: s=min(s,sum(b))

print(s)