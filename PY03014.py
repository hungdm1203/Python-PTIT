# bieu thuc


for _ in range(int(input())):
    li=list(i for i in input() if i=='(' or i==')')
    dem=1
    a=[]
    for i in range(len(li)):
        if li[i]=='(':
            print(dem,end=" ")
            a.append(dem)
            dem+=1
        else:
            print(a[-1],end=" ")
            a.pop(-1)
    print()