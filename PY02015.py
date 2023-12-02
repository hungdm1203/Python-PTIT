# bien doi day so

while True:
    li=list(int(i) for i in input().split())
    if all(i==0 for i in li):
        break
    dem=0
    while not all(li[i]==li[i+1] for i in range(0,3)):
        dem+=1
        a=li[0]
        for j in range(0,3):
            li[j]=abs(li[j]-li[j+1])
        li[3]=abs(li[3]-a)
    print(dem)