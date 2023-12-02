# xu ly xau ky tu

a=set(i.lower() for i in input().split())
b=set(i.lower() for i in input().split())
l1=list(a.union(b))
l2=list(a.intersection(b))
l1.sort()
l2.sort()
print(" ".join(l1))
print(" ".join(l2))