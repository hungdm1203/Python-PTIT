# khoang cach nguyen to

def nto(n):
    return n>1 and all(n%i!=0 for i in range(2,int(n**0.5)+1))

n,x=map(int,input().split())
li=[2]
res=3
while(len(li)<n):
    if nto(res):
        li.append(res)
    res+=2
print(x,end=" ")
for i in li:
    x=x+i
    print(x,end=" ")