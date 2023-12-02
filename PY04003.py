# lop phan so 1

import math
class Pso:
    def __init__(self,x,y) :
        self.x=x
        self.y=y

    def rutgon(self):
        GCD=math.gcd(self.x,self.y)
        self.x=self.x//GCD
        self.y=self.y//GCD
    
    def __str__(self) :
        return f"{self.x}/{self.y}"
    
a,b=map(int,input().split())
pso=Pso(a,b)
pso.rutgon()
print(pso.__str__())