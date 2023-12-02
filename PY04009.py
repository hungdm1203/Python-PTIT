# lop so phuc

class SoPhuc:
    def __init__(self,x,y) -> None:
        self.x=x
        self.y=y
    
    def add(self,other):
        return SoPhuc(self.x+other.x,self.y+other.y)
    
    def mul(self,other):
        a=self.x*other.x-self.y*other.y
        b=self.y*other.x+self.x*other.y
        return SoPhuc(a,b)

    def toString(self):
        s=f"{self.x}"
        if self.y>0:
            s=s+f" + {self.y}i"
        elif self.y<0:
            s=s+f" - {abs(self.y)}i"
        return s




for _ in range(int(input())):
    li=[int(i) for i in input().split()]
    sp1=SoPhuc(li[0],li[1])
    sp2=SoPhuc(li[2],li[3])
    spC=sp1.add(sp2).mul(sp1)
    spD=(sp1.add(sp2)).mul(sp1.add(sp2))
    print(f"{spC.toString()}, {spD.toString()}")


    