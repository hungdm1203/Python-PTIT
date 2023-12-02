# kiem tra nguyen to


def nto(n):
    return n>1 and all(n%i!=0 for i in range(2,int(n**0.5)+1))

n,m=map(int,input().split())
a=[]
for i in range(n):
    li=[int(i) for i in input().split()]
    a.append(li)
for i in a:
    for j in i:
        if nto(j):
            print(1,end=" ")
        else: print(0,end=" ")
    print()