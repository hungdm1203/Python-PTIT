# phan hoach dan cu

for _ in range(int(input())):
    n,x,y=map(int,input().split())
    a=[int(i) for i in input().split()]
    a.sort(reverse=True)
    c=min(x,y)
    d=max(x,y)
    s1=sum(a[:c])
    s2=sum(a[c:c+d])
    print(f"{(s1/c+s2/d):.6f}")