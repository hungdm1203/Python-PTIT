# tinh diem trung binh


n=int(input())
li=list(float(i) for i in input().split())
li.sort()
sum=0
dem=0
for i in li:
    if i!=li[0] and i!=li[-1]:
        dem+=1
        sum+=i
print(round(sum/dem,2))

