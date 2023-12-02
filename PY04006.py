# lop triangle 2


import math
class Point:
    def __init__(self,x,y) :
        self.x=x
        self.y=y

    def distance(self,other):
        return math.sqrt((self.x-other.x)**2+(self.y-other.y)**2)
    

class Triangle:
    def __init__(self,A,B,C):
        self.A=A
        self.B=B
        self.C=C

    def check(self):
        AB=self.A.distance(self.B)
        AC=self.A.distance(self.C)
        BC=self.B.distance(self.C)
        if AB+AC<=BC or AB+BC<=AC or AC+BC<=AB:
            return 'INVALID'
        else: 
            S=((AB+AC+BC)*(AB+AC-BC)*(AB-AC+BC)*(-AB+AC+BC))**0.5/4.0
            return "{:.2f}".format(S)
    

a=[]
t=int(input())
for j in range(t):
    a+=[float(i) for i in input().split()]

i = 0
for index in range(t):
    triagle = Triangle(Point(a[i], a[i+1]), Point(a[i+2], a[i+3]), Point(a[i+4], a[i+5]))
    print(triagle.check())
    i += 6