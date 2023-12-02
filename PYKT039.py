# day so phu hop

for _ in range(int(input())):
    n=input()
    l1=[int(i) for i in input().split()]
    l2=[int(i) for i in input().split()]
    check=1
    while check==1 and len(l1)>0:
        a=min(l1)
        b=min(l2)
        if a>b:
            check=0
            break
        else:
            l1.remove(a)
            l2.remove(b)
    if check==1:
        print("YES")
    else: print("NO")