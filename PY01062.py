# uu the nguyen to

def nto(n):
    return n>1 and all(n%i!=0 for i in range(2,int(n**0.5)+1))

for _ in range(int(input())):
    li=list(int(i) for i in input())
    tmp=0
    for i in li:
        if nto(i): tmp+=1
    if tmp>len(li)-tmp and nto(len(li)):
        print("YES")
    else: print("NO")