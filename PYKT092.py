# diem tuyen sinh

class ThiSinh:
    def __init__(self,id,name,score,dt,kv) -> None:
        self.id='TS{:02d}'.format(id)
        self.name=name
        self.score=score
        self.dt=dt
        self.kv=kv
        if self.kv==1: self.score+=1.5
        elif self.kv==2: self.score+=1

        if self.dt!="Kinh": self.score+=1.5

        if self.score>=20.5: self.note="Do"
        else: self.note="Truot"

    def __str__(self) -> str:
        return f"{self.id} {self.name} {self.score} {self.note}"
    

a=[]
for i in range(int(input())):
    name=input().upper().split()
    for j in range(len(name)):
        name[j]=name[j].title()
    res=" ".join(name)
    a.append(ThiSinh(i+1,res,float(input()),input(),int(input())))

a.sort(key=lambda i:i.score,reverse=True)
for i in a: print(i)

