# sap xep lich thi

from datetime import datetime

class Mon:
    def __init__(self,id,name,type) -> None:
        self.id=id
        self.name=name
        self.type=type

class Cathi(Mon):
    def __init__(self,id,date,time,room) -> None:
        self.id="C{:03d}".format(id)
        self.date=date
        self.time=time
        self.room=room
        self.strd=datetime.strptime(date, "%d/%m/%Y")
        self.strt=datetime.strptime(time, "%H:%M")    
    def update(self,m,group,quantity):
        self.m=m
        self.group=group
        self.quantity=quantity
    def __str__(self) -> str:
        return f"{self.date} {self.time} {self.room} {self.m.name} {self.group} {self.quantity}"


f1=open("MONTHI.in",'r')
f2=open("CATHI.in",'r')
f3=open("LICHTHI.in",'r')
n=int(f1.readline())
a={}
for i in range(n):
    id=f1.readline().strip()
    a[id]=Mon(id,f1.readline().strip(),f1.readline().strip())

b={}
n=int(f2.readline())
for i in range(n):
    id="C{:03d}".format(i+1)
    b[id]=Cathi(i+1,f2.readline().strip(),f2.readline().strip(),f2.readline().strip())

n=int(f3.readline())
res=[]
for i in range(n):
    li=f3.readline().split()
    b[li[0]].update(a[li[1]],li[2],int(li[3]))
    res.append(b[li[0]])

res.sort(key=lambda i:(i.strd,i.strt,i.id))
for i in res:print(i)