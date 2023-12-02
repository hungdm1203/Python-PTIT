# so tang giam


def check(n):
    li=list(int(i) for i in n)
    if len(li)<3:
        return "NO"
    c=1
    for i in range(len(li)-1):
        if c==1 and li[i]>=li[i+1]:
            c=0
        elif c==0 and li[i]<=li[i+1]:
            return "NO"
    return "YES"

for _ in range(int(input())):
    n=input()
    check(n)
    print(check(n))

   