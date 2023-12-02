# danh sach email

ip=open("CONTACT.in",'r')
line=ip.read().split()
a=[]
for i in line:
    if i.lower() not in a:
        a.append(i.lower())

a.sort()
for i in a:
    print(i)