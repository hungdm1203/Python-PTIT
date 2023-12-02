# emirp number


def nto(n):
    return n>1 and all(n%i!=0 for i in range(2,int(n**0.5)+1))


def check(n):
    li=[]
    for i in range(13,n):
        if nto(i) and nto(int(str(i)[::-1])) and str(i)!=str(i)[::-1] and int(str(i)[::-1])<n:
            if i not in li:
                li.append(i)
            if int(str(i)[::-1]) not in li:
                li.append(int(str(i)[::-1]))
    print(*li)


for _ in range(int(input())):
    n=int(input())
    check(n)