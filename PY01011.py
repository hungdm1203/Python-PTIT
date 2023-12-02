# liet ke so dep


def check(n):
    return str(n)==str(n)[::-1] and all(int(i)%2==0 for i in str(n)) and len(str(n))%2==0

for _ in range(int(input())):
    n=int(input())
    for i in range(10,n):
        if check(i):
            print(i,end=" ")
    print()