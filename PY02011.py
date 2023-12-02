# bien doi va day bang nhau

n=int(input())
a=[int(i) for i in input().split()]
id=0
mi=sum(a)

for i in range(n):
    s=0
    for j in range(n):
        s+=abs(a[i]-a[j])
    if s<mi:
        mi=s
        id=i

print(f"{mi} {a[id]}")