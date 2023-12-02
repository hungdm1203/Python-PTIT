# chan-le

for _ in range(int(input())):
    a=list(int(i) for i in input())
    check=1
    if sum(a)%10!=0:
        check=0
    for i in range(len(a)-1):
        if abs(a[i]-a[i+1])!=2:
            check=0
            break
    if check==1:
        print("YES")
    else: print("NO")