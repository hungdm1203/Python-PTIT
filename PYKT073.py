# xac dinh the loai tho

a=[]
res=[]
dem=0
for _ in range(int(input())):
    li=input().split()
    if len(a)==0 and len(li)==6: res.append(1)
    if len(a)>1 and a[-1]==7 and len(li)==6: res.append(1)
    a.append(len(li))
    if len(li)==7 and dem==0: res.append(2)
    if len(li)==7: dem+=1
    if len(li)==7 and dem%4==0: dem=0

print(len(res))
for i in res: print(i)