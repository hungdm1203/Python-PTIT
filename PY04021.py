# tinh toan thoi gian


class Gamer:
    def __init__(self,id,name,times) -> None:
        self.id=id
        self.name=name 
        self.times=times 
    
    def str(self):
        return f"{self.id} {self.name} {self.times//60} gio {self.times%60} phut"
    


dsGamer=[]
for _ in range(int(input())):
    id=input()
    name=input()
    start=[int(i) for i in input().split(':')]
    end=[int(i) for i in input().split(':')]
    times=end[0]*60+end[1]-start[0]*60-start[1]
    gamer=Gamer(id,name,times)
    dsGamer.append(gamer)

dsGamer.sort(key=lambda i:i.times,reverse=True)

for i in dsGamer:
    print(i.str())