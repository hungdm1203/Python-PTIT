# loai bo so nguyen



file=open('DATA.in','r')
li=[]
for i in file:
    for j in i.split():
        if not j.isdigit() or int(j)<-2**31 or int(j)>2**31:
            li.append(j)

li.sort()
print(*li)