# so thuan nghich chan


def check(n):
    for j in range(22,n,22):
        li=list(int(i) for i in str(j))
        if li==li[::-1] and all(i%2==0 for i in li) and len(li)%2==0:
            print(''.join(str(i) for i in li),end=" ")


for _ in range(int(input())):
    n=int(input())
    check(n)
    print()