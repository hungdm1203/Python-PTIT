# lop phan so 2


import math

class Pso:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def rutgon(self):
        GCD=math.gcd(self.x,self.y)
        self.x=self.x//GCD
        self.y=self.y//GCD
    
    def __add__ (self,other):
        LCM=math.lcm(self.y,other.y)
        a=self.x*(LCM//self.y) + other.x*(LCM//other.y)
        b=LCM
        pso3=Pso(a,b)
        pso3.rutgon()
        return pso3
    
    def __str__(self):
        return f"{self.x}/{self.y}"
    
    
    

li=list(int(i) for i in input().split())
pso1=Pso(li[0],li[1])
pso2=Pso(li[2],li[3])
pso3=pso1+pso2
print(pso3.__str__())
