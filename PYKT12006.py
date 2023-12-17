# khuyen mai

n,k=map(int,input().split())
a=[int(i) for i in input().split()]
b=[int(i) for i in input().split()]
res=[[]]*n
for i in range(n):
    res[i]=[a[i],b[i]]


s=0
res.sort(key=lambda i:(i[0]-i[1],i[0]))
for i in range(k):
    s+=res[i][0]

tmp=k
for i in range(k,n):
    if res[i][0]<res[i][1]: 
        s+=res[i][0]
        tmp=i+1
        
for i in range(tmp,n):
    s+=res[i][1]

print(s)
