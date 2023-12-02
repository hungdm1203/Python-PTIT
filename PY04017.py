# tinh van toc
class Cuaro:
    def __init__(self,name,add,end) -> None:
        self.id=""
        self.name=name
        self.add=add
        self.end=end
        a=[int(i) for i in end.split(":")]
        self.time=(a[0]-6)*60+a[1]
        self.v=round(120*60/self.time)
        for i in self.add.split(): self.id+=i[0]
        for i in self.name.split(): self.id+=i[0]
    
    def __str__(self) -> str:
        return f"{self.id} {self.name} {self.add} {self.v} Km/h"


a=[]
for _ in range(int(input())):
    c=Cuaro(input(),input(),input())
    a.append(c)
    
a.sort(key=lambda x: x.time)
for i in a: print(i)

