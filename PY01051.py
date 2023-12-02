# tong chu so thuan nghich

for _ in range(int(input())):
    li=list(int(i) for i in input())
    s=sum(li)
    if s>10 and str(s)==str(s)[::-1]:
        print("YES")
    else: print("NO")