# sap xep nguyen to

nto=[1]*1001
nto[0]=nto[1]=0
for i in range(2,int(1001**0.5)):
    if nto[i]==1:
        for j in range(i*i,1001,i):
            nto[j]=0

n=int(input())
a=[int(i) for i in input().split()]

for i in range(n):
    if nto[a[i]]==1:    
        for j in range(i+1,n):
            if nto[a[j]]==1 and a[i]>a[j]:
                tmp=a[i]
                a[i]=a[j]
                a[j]=tmp

print(*a)
