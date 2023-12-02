# dia chi ip

for _ in range(int(input())):
    li=list(i for i in input().split('.'))
    if all(i.isdigit() and int(i)>=0 and int(i)<=255 and len(i)<=3 for i in li) and len(li)==4:
        print("YES")
    else: print("NO")