# danh sach phim
from datetime import datetime

class Type:
    def __init__(self,idType,nameType) -> None:
        self.idType=idType
        self.nameType=nameType


class Phim(Type):
    def __init__(self, id,t,date,name,soTap) -> None:
        self.id="P{:03d}".format(id)
        self.tid=t.idType
        self.tname=t.nameType
        self.dateStr=date
        self.date=datetime.strptime(date,"%d/%m/%Y")
        self.name=name
        self.sotap=soTap
    
    def __str__(self) -> str:
        return f"{self.id} {self.tname} {self.dateStr} {self.name} {self.sotap}"
    

n,m=map(int,input().split())
listT={}
listP=[]
for i in range(n):
    id="TL{:03d}".format(i+1)
    s=input()
    listT[id]=Type(id,s)

for i in range(m):
    s=input()
    listP.append(Phim(i+1,listT[s],input(),input(),int(input())))
    

listP.sort(key=lambda i: (i.date,i.name))
# listP.sort(key=lambda i:i.sotap,reverse=True)

for i in listP: print(i)

