# dau cuoi nguyen to


def nto(n):
    return n>1 and all(n%i!=0 for i in range(2,int(n**0.5)+1))

for _ in range(int(input())):
    s=input()
    if nto(int(s[:3])) and nto(int(s[-3::1])):
        print("YES")
    else: print("NO")