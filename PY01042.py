# kiem tra he co so 3

for _ in range(int(input())):
    li=list(i for i in input())
    c=0
    if all((i=='0' or i=='1' or i=='2') for i in li):
        c=1
    if c==1:
        print("YES")
    else: print("NO")