# tinh tong 1

for _ in range(int(input())):
    n,k=map(int,input().split())
    res=0
    for i in range(1,n+1):
        res=(res+i**k%(10**9+7))%(10**9+7)
    print(res)