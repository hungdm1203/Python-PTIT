# tinh can doi cua ma tran-1

a=[]
for _ in range(int(input())):
    tmp=[int(i) for i in input().split()]
    a.append(tmp)

k=int(input())
x=0
y=0

for i in range(len(a)):
    for j in range(len(a)):
        if j>i: x+=a[i][j]
        if j<i: y+=a[i][j]

if abs(x-y)<=k:
    print("YES")
else: print("NO")
print(abs(x-y))

