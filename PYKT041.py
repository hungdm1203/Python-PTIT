# dem cap dong xu


a=[]
dem=0
n=int(input())
for _ in range(n):
    a.append(input())

res=0
for i in range(n):
    for j in range(n):
        if a[i][j]=='C':
            for k in range(i+1,n): 
                if a[k][j]=='C': res+=1
            for k in range(j+1,n):
                if a[i][k]=='C': res+=1
print(res)