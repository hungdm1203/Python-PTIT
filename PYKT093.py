# tinh diem trung binh

import math

def build(s):
    li=s.split()
    for i in range(len(li)):
        li[i]=li[i].title()
    return " ".join(li)

class SV:
    def __init__(self,id,name,a,b,c) -> None:
        self.id="SV{:02d}".format(id)
        self.name=name
        self.a=a
        self.b=b
        self.c=c
        self.tb=math.ceil((a*3+b*3+c*2)*100/8)/100

    def __str__(self) -> str:
        return f"{self.id} {self.name} {self.tb:.2f} {self.rank}"
    

a=[]
for i in range(int(input())):
    name=input()
    a.append(SV(i+1,build(name),float(input()),float(input()),float(input())))

a.sort(key=lambda i:(-i.tb,i.id))

dem=1
tmp=a[0]
tmp.rank=1
for i in a:
    if tmp.tb==i.tb:
        i.rank=tmp.rank
    else: i.rank=dem
    print(i)
    dem+=1