# prime_triplet

def nto(n):
    return n>1 and all(n%i!=0 for i in range(2,int(n**0.5)+1))

for _ in range(int(input())):
    n=int(input())
    dem=0
    for i in range(2,n-6):
        if nto(i) and nto(i+6):
            if nto(i+2) or nto(i+4):
                dem+=1
    print(dem)