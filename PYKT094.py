# tinh luong

class PhongBan:
    def __init__(self,id,name) -> None:
        self.id=id
        self.name=name

class NhanVien(PhongBan):
    def __init__(self,id,name,p,lcb,nc) -> None:
        self.id=id
        self.name=name
        self.lcb=lcb
        self.nc=nc
        self.pb=p.name
        self.sum=self.tinhLuong()*1000

    def tinhLuong(self):
        if self.id[0]=="A":
            if int(self.id[1:3])>=16:
                return self.lcb*self.nc*20
            elif int(self.id[1:3])>=9:
                return self.lcb*self.nc*14
            elif int(self.id[1:3])>=4:
                return self.lcb*self.nc*12
            else: return self.lcb*self.nc*10
        elif self.id[0]=="B":
            if int(self.id[1:3])>=16:
                return self.lcb*self.nc*16
            elif int(self.id[1:3])>=9:
                return self.lcb*self.nc*13
            elif int(self.id[1:3])>=4:
                return self.lcb*self.nc*11
            else: return self.lcb*self.nc*10
        elif self.id[0]=="C":
            if int(self.id[1:3])>=16:
                return self.lcb*self.nc*14
            elif int(self.id[1:3])>=9:
                return self.lcb*self.nc*12
            elif int(self.id[1:3])>=4:
                return self.lcb*self.nc*10
            else: return self.lcb*self.nc*9
        else:
            if int(self.id[1:3])>=16:
                return self.lcb*self.nc*13
            elif int(self.id[1:3])>=9:
                return self.lcb*self.nc*11
            elif int(self.id[1:3])>=4:
                return self.lcb*self.nc*9
            else: return self.lcb*self.nc*8


    def __str__(self) -> str:
        return f"{self.id} {self.name} {self.pb} {self.sum}"
    

listPB={}
listNV=[]
for _ in range(int(input())):
    s=input()
    i=s.index(" ")
    listPB[s[:i]]=PhongBan(s[:i],s[i+1:])

for _ in range(int(input())):
    id=input()
    listNV.append(NhanVien(id,input(),listPB[id[-2:]],int(input()),int(input())))

for i in listNV: print(i)

# 2
# HC Hanh chinh
# KH Ke hoach Dau tu
# 2
# C06HC
# Tran Binh Minh
# 65
# 25
# D03KH
# Le Hoa Binh
# 59
# 24