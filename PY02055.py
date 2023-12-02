# so nguyen to lon nhat trong ma tran

def isPrime(n):
    return n>=2 and all(n%i!=0 for i in range(2,int(n**0.5)+1))

n,m=map(int,input().split())
a=[]
ma=0
for _ in range(n):
    li=[int(i) for i in input().split()]
    a.append(li)
    for j in li:
        if isPrime(j): ma=max(j,ma)

if ma==0: print("NOT FOUND")
else:
    print(ma)
    for i in range(n):
        for j in range(m):
            if a[i][j]==ma:
                print(f"Vi tri [{i}][{j}]")

