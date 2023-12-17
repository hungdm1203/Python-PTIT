# danh sach ca thi

from datetime import datetime

class CaThi:
    def __init__(self,id,date,time,room) -> None:
        self.id="C{:03d}".format(id)
        self.date=date
        self.time=time
        self.room=room
        self.sd=datetime.strptime(date, "%d/%m/%Y")
        self.st=datetime.strptime(time, "%H:%M")

    def __str__(self) -> str:
        return f"{self.id} {self.date} {self.time} {self.room}"

file=open("CATHI.in",'r')
n=int(file.readline())
a=[]
for i in range(n):
    a.append(CaThi(i+1,file.readline().strip(),file.readline().strip(),file.readline().strip()))

a.sort(key=lambda i: (i.sd,i.st,i.id))
for i in a: print(i)