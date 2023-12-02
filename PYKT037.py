# doi co so

def build(n,b):
    s=""
    while n>0:
        n,a=divmod(n,b) #n=n//b a=n%b
        if a<10:
            s=str(a)+s
        else:
            s=chr(65+a-10)+s
    return s


for _ in range(int(input())):
    n,b=map(int,input().split())
    print(build(n,b))