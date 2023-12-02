# bang diem


class SinhVien:
    def __init__(self,id,name, dtb) -> None:
        self.id=id
        self.name=name
        self.dtb=dtb


    def xepLoai(self):
        if self.dtb>=9.0:
            return "XUAT SAC"
        elif self.dtb>=8.0:
            return "GIOI"
        elif self.dtb>=7.0:
            return "KHA"
        elif self.dtb>=5.0:
            return "TB"
        else: return "YEU"

    def __str__(self) -> str:
        return f"{self.id} {self.name} {round(self.dtb,1)} {self.xepLoai()}"


dem=1
svList=[]
for _ in range(int(input())):
    name=input()
    score=[float(i) for i in input().split()]
    dtb=(2*sum(score[:2])+sum(score[2:]))/10/1.2
    if dem<10:
        id='HS0'+str(dem)
        sv=SinhVien(id,name,round(dtb,1))
        svList.append(sv)
        dem+=1
    else:
        id='HS'+str(dem)
        sv=SinhVien(id,name,round(dtb,1))
        svList.append(sv)
        dem+=1

svList.sort(key=lambda i: i.dtb,reverse=True)
for i in svList:
    print(i.__str__())