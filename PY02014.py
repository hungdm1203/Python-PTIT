# bien doi nguyen to

li=[1]*10001
li[0]=li[1]=0
for i in range(2,int(10001**0.5)):
    if li[i]==1:
        for j in range(i*i,10001,i):
            li[j]=0

n=int(input())
a=[int(i) for i in input().split()]
s=0
for i in a:
    tmp=10001
    if li[i]==0:
        for j in range(len(li)):
            if li[j]==1: tmp=min(tmp,abs(j-i))
    if tmp!=10001: s=max(s,tmp)

print(s)