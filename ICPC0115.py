# so krish

def gthua(n):
    mul=1
    for i in range(1,n+1):
        mul*=i
    return mul

for _ in range(int(input())):
    n=int(input())
    li=list(gthua(int(i)) for i in str(n))
    if sum(li)==n:
        print("Yes")
    else: print("No")
