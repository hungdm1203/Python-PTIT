# phan chia nguyen to

def check(n):
    return n>=2 and all(n%i!=0 for i in range(2,int(n**0.5)+1))

n=input()
a=[int(i) for i in input().split()]
b=[]
for i in a:
    if i not in b: b.append(i)

ok=0
s=sum(b)
tmp=0
for i in range(len(b)):
    tmp+=b[i]
    if check(tmp) and check(s-tmp):
        print(i)
        ok=1
        break

if ok==0: print("NOT FOUND")