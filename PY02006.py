# day so phu hop


def check(a,b):
    for i in range(len(a)):
        if a[i]>b[i]:
            return "NO"
    return "YES"


for _ in range(int(input())):
    n=int(input())
    a=list(int(i) for i in input().split())
    a.sort()
    b=list(int(i) for i in input().split())
    b.sort()
    print(check(a,b))