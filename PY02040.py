# ma tran-2

n=int(input())
tren=0
duoi=0
for i in range(n):
    li=list(int(j) for j in input().split())
    tren+=sum(li[j] for j in range(n) if j<n-i-1)
    duoi+=sum(li[j] for j in range(n) if j>n-i-1)

k=int(input())
if k>=abs(tren-duoi):
    print('YES')
else: print('NO')
print(abs(tren-duoi))
