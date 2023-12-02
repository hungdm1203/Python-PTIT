# tuyen nhan vien

class ThiSinh:
    def __init__(self,id,name,score) -> None:
        self.id='TS0{}'.format(id)
        self.name=name
        self.score=score

    def xepLoai(self):
        if self.score>9.5:
            return "XUAT SAC"
        elif self.score >=8.0:
            return "DAT"
        elif self.score>=5.0:
            return "CAN NHAC"
        else: return "TRUOT"
    
    def __str__(self) -> str:
        return f"{self.id} {self.name} {self.score:.2f} {self.xepLoai()}" 
    

dsThiSinh=[]
for i in range(int(input())):
    name=input()
    lt=float(input())
    th=float(input())
    if lt>10:
        lt=lt/10
    if th>10:
        th=th/10
    ts=ThiSinh(i+1,name,(lt+th)/2)
    dsThiSinh.append(ts)

dsThiSinh.sort(key=lambda i:i.score,reverse=True)
for i in dsThiSinh:
    print(i.__str__())