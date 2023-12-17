# danh sach thi lap trinh

class Team:
    def __init__(self,id,name,school) -> None:
        self.id="Team{:02d}".format(id)
        self.name=name
        self.school=school
    
class TS(Team):
    def __init__(self, id, name, t) -> None:
        self.id="C{:03d}".format(id)
        self.name=name
        self.t=t
    
    def __str__(self) -> str:
        return f"{self.id} {self.name} {self.t.name} {self.t.school}"
    
listT={}
listTS=[]
for i in range(int(input())):
    id="Team{:02d}".format(i+1)
    listT[id]=Team(i+1,input(),input())

for i in range(int(input())):
    name=input()
    team=input()
    listTS.append(TS(i+1,name,listT[team]))

listTS.sort(key=lambda i:(i.name))
for i in listTS: print(i)