# ky tu thu k


# cach 1
# for _ in range(int(input())):
#     n,k=map(int,input().split())
#     s='A'
#     for i in range(1,n):
#         tmp=s+chr(65+i)+s
#         s=tmp
#     print(s[k-1])


# cach 2

def ktao():
    for i in range(2,27):
        li.append(li[i-1]*2)

li=[0,1]
for _ in range(int(input())):
    ktao()
    n,k=map(int,input().split())
    for i in range(n,0,-1):
        if k>li[i]:
            k=k-li[i]
        elif k==li[i]:
            print(chr(65+i-1))
