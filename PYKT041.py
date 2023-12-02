# dem cap dong xu


a=[]
dem=0
for _ in range(int(input())):
    a.append(input())

res=0
for i in range(len(a)):
    tmp=0
    for j in range(len(a[i])):
        if a[i][j]=='C':
            res+=tmp
            tmp+=1

for i in range(len(a)):
    tmp=0
    for j in range(len(a[i])):
        if a[j][i]=='C':
            res+=tmp
            tmp+=1

print(res)
