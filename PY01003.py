# lam tron so

for _ in range(int(input())):
    li=list(int(i) for i in input())
    a=0
    for i in range(len(li)-1,-1,-1):
        if a>=5:
            a=li[i]+1
            li[i]=0
        else:
            a=li[i]
            li[i]=0
    li[0]=a
    print("".join(str(i) for i in li))       