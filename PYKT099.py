# hieu cua hai tap tu

f1=open("DATA1.in",'r')
f2=open("DATA2.in",'r')
a=[]
b=[]
for i in f1:
    for j in i.lower().split():
        if j not in a: a.append(j)

for i in f2:
    for j in i.lower().split():
        if j not in b: b.append(j)

a.sort()
b.sort()
c=[i for i in a if i not in b]
d=[i for i in b if i not in a]
print(*c)
print(*d)