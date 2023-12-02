# so khong giam

for _ in range(int(input())):
    li=list(i for i in input())
    check=1
    for i in range(len(li)-1):
        if li[i]>li[i+1]:
            print('NO')
            check=0
            break
    if check==1: print('YES')
