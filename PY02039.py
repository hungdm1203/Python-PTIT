# ma tran 1

n=int(input())
tren=0
duoi=0
for i in range(n):
    li=list(int(i) for i in input().split())
    tren+=sum(li[j] for j in range(n) if i<j)
    duoi+=sum(li[j] for j in range(n) if i>j)
k=int(input())
if abs(tren-duoi)<=k:
    print('YES')
    print(abs(tren-duoi))
else: 
    print("NO")
    print(abs(tren-duoi))