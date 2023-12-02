# xac dinh trung tuyen

class GiaoVien:
    def __init__(self,id,name,sub,tinHoc,chuyenMon) -> None:
        self.id='GV{:02d}'.format(id)
        self.name=name
        if sub[0]=='A': self.sub="TOAN"
        elif sub[0]=='B': self.sub="LY"
        else: self.sub="HOA"
        self.tinHoc=tinHoc
        self.chuyenMon=chuyenMon
        self.tong=self.tinHoc*2+self.chuyenMon
        if int(sub[1])==1: self.tong+=2
        elif int(sub[1])==2: self.tong+=1.5
        elif int(sub[1])==3: self.tong+=1
        if self.tong>=18: self.note="TRUNG TUYEN"
        else: self.note="LOAI"

    def __str__(self) -> str:
        return f"{self.id} {self.name} {self.sub} {self.tong:.1f} {self.note}"


a=[]
for i in range(int(input())):
    gv=GiaoVien(i+1,input(),input(),float(input()),float(input()))
    a.append(gv)

a.sort(key=lambda i:i.tong,reverse=True)
for i in a: print(i)
