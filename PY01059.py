# tong chu so-tich chu so

for _ in range(int(input())):
    li=list(int(i) for i in input())
    sum=0
    for i in range(0,len(li),2):
        sum+=li[i]
    if all(li[i]==0 for i in range(1,len(li),2)):
        print(f"{sum} 0")
    else:
        mul=1
        for i in range(1,len(li),2):
            if li[i]!=0:
                mul=mul*li[i]
        print(f"{sum} {mul}")