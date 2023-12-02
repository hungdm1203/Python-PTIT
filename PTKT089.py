# sap xep chan le

n=int(input())
a=list(int(i) for i in input().split())
a1=[i for i in a if i%2!=0]
a2=[i for i in a if i%2==0]
tmp=min(len(a1),len(a2))
a1.sort(reverse=True)
a2.sort()
for i in range(n):
    pass