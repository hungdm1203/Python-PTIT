# giai ma

for _ in range(int(input())):
    li=list(i for i in input())
    s=""
    for i in range(0,len(li),2):
        s=s+li[i]*int(li[i+1])
    print(s)