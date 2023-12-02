# xoay mang

for _ in range(int(input())):
    n,k=map(int,input().split())
    li=list(int(i) for i in input().split())
    k=k%len(li)
    a=li[k:]+li[:k]
    print(*a)