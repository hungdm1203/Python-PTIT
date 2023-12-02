# liet ke so nguyen to trong day


def isPrime(n):
    return n>1 and all(n%i!=0 for i in range(2,int(n**0.5)+1))

n=int(input())
li=list(int(i) for i in input().split())
a=[]
for i in li:
    if isPrime(i) and i not in a:
        print(f"{i} {li.count(i)}")
        a.append(i)