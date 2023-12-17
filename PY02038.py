# dem cap dong xu

n=int(input())
a=[]
for _ in range(n):
    a.append(input())

res=0
for i in range(n):
    for j in range(n):
        if a[i][j]=="C":
            for k in range(j+1,n): 
                if a[i][k]==a[i][j]: res+=1
            for k in range(i+1,n): 
                if a[k][j]==a[i][j]: res+=1

print(res)