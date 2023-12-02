# lap hoa don-2
from datetime import datetime
class HoaDon:
    def __init__(self,id,name,room,vao,ra,dvu) -> None:
        self.id="KH{:02d}".format(id)
        self.name=name
        self.room=room
        self.vao=datetime.strptime(vao,"%d/%m/%Y")
        self.datein=vao
        self.ra=datetime.strptime(ra,"%d/%m/%Y")
        self.dateout=ra
        self.price=dvu
        self.time=abs((self.ra-self.vao).days)+1
        if self.room[0]=='1': self.price=self.price+25*self.time
        elif self.room[0]=='2': self.price=self.price+34*self.time
        elif self.room[0]=='3': self.price=self.price+50*self.time
        else: self.price=self.price+80*self.time

    def __str__(self) -> str:
        return f"{self.id} {self.name} {self.room} {self.time} {self.price}"

a=[]        
for i in range(int(input())):
    hd=HoaDon(i+1,input().rstrip(),input().rstrip(),input().rstrip(),input().rstrip(),int(input()))
    a.append(hd)

a.sort(key=lambda i:i.price,reverse=True)

for i in a: print(i)
