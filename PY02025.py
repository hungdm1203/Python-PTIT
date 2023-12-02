# tap hop so nguyen

n,m=map(int,input().split())
a=set(int(i) for i in input().split())
b=set(int(i) for i in input().split())
c=[i for i in a if i in b]
d=[i for i in a if i not in b]
e=[i for i in b if i not in a]
print(*c.sort())
print(*d.sort())
print(*e.sort())