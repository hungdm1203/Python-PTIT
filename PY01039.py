# kiem tra so dep


def check(n):
    c=1
    li=list(i for i in n)
    for i in range(len(li)-2):
        if li[i]!=li[i+2]:
            c=0
            break
    if len(set(li))==2 and c==1:
        print("YES")
    else: print("NO")

for _ in range(int(input())):
    n=input()
    check(n)