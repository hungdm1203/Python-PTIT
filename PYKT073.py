# xac dinh the loai tho


a=[]
res=[]
check=0
for _ in range(int(input())):
    li=input().split()
    if len(li)==6 and len(a)==0:
        res.append(1) 
    a.append(len(li))
    if len(a)>1 and len(li)==6 and a[-2]==7:
        res.append(1)

    if len(li)==7 and len(a)==0:
        res.append(2)
    if len(li)==7: check+=1
    if check==4:
        res.append(2)
        check=0

print(len(res))
for i in res:
    print(i)



