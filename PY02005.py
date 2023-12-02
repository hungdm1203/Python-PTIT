# cap nghich the

n=int(input())
li=list(int(i) for i in input().split())
dem=0
for i in range(n):
    for j in range(i+1,n):
        if li[i]>li[j]:
            dem+=1
print(dem)