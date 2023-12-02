# perfect prime


def nto(n):
    return n>1 and all(n%i!=0 for i in range(2,int(n**0.5)+1))


def check(n):
    li=list(int(i) for i in str(n))
    if nto(n) and nto(int(str(n)[::-1])) and nto(sum(li)) and all(nto(i) for i in li):
        print("Yes")
    else: print("No")


for _ in range(int(input())):
    n=int(input())
    check(n)