# min triple

for _ in range(int(input())):
    n=int(input())
    a=[int(i) for i in input().split()]
    x=3
    s=0
    while x>0:
        tmp=min(a)
        a.remove(tmp)
        x-=1
        s+=tmp
    print(s)