# tinh diem chuyen can


class SinhVien:
    score=0
    def __init__(self,msv,name,lop) -> None:
        self.msv=msv
        self.name=name
        self.lop=lop
        self.score=10

    def cal(self,s):
        m=li[1].count('m')
        v=li[1].count('v')
        if 10-m-2*v<=0:
            self.score=0
        else: self.score=10-m-2*v


    def __str__(self) -> str:
        s=""
        if self.score==0:
            s="KDDK"
        return f"{self.msv} {self.name} {self.lop} {self.score} {s}"
    

dsSV=[]
dsMSV=[]
n=int(input())
for _ in range(n):
    msv=input()
    dsMSV.append(msv)
    sv=SinhVien(msv,input(),input())
    dsSV.append(sv)
    


for _ in range(n):
    li=list(input().split())
    i=dsMSV.index(li[0])
    dsSV[i].cal(li[1])

for i in dsSV:
    print(i.__str__())