# danh sach thi lap trinh

class Team:
    def __init__(self,id,name,school) -> None:
        self.id=id
        self.name=name
        self.school=school

class ThiSinh(Team):
    def __init__(self, id, name, t) -> None:
        self.id="C{:03d}".format(id)
        self.name=name
        self.t=t

    def __str__(self) -> str:
        return f"{self.id} {self.name} {self.t.name} {self.t.school}"
    

lT={}
lTS=[]
for i in range(int(input())):
    id="Team{:02d}".format(i+1)
    lT[id]=Team(id,input(),input())

for i in range(int(input())):
    name=input()
    t=input()
    lTS.append(ThiSinh(i+1,name,lT[t]))

lTS.sort(key=lambda i: i.name)
for i in lTS: print(i)

