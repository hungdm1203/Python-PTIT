# day so nhi phan

n=input()
li=list(int(i) for i in input().split())
dem=0
for i in range(len(li)-1):
    if li[i]!=li[i+1]: dem+=1
print(dem)