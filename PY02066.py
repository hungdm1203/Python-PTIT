# bai toan dem

n=int(input())
a=[]
while len(a)<n:
    a.extend(int(i) for i in input().split())

ok=1
for i in range(1,a[n-1]):
    if i not in a:
        print(i)
        ok=0

if ok==1: print("Excellent!")