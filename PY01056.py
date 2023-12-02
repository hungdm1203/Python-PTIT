# chan -le nguyen to


def nto(n):
    return n>1 and all(n%i!=0 for i in range(2,int(n**0.5)+1))


for _ in range(int(input())):
    li=list(int(i) for i in input())
    check=1
    for i in range(len(li)):
        if i%2==0 and li[i]%2!=0:
            check=0
            break
        if i%2!=0 and li[i]%2==0:
            check=0
            break
    if check==1 and nto(sum(li)):
        print("YES")
    else: print("NO")