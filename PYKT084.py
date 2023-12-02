# cau hoi theo chu de-1

a=[]
for i in range(int(input())):
    a.append(input())

res={}
tmp=0
for i in range(len(a)):
    if a[i]=="": 
        res[a[tmp]]=i-tmp-1
        tmp=i+1

res[a[tmp]]=len(a)-tmp-1

for i in res: print(f"{i}: {res[i]}")

