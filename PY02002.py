# liet so fibonacci


fib=[1,1]
for i in range(2,92):
    fib.append(fib[i-1]+fib[i-2])


for _ in range(int(input())):
    a,b=map(int,input().split())
    for i in range(a,b+1):
        print(fib[i-1],end=" ")
    print()