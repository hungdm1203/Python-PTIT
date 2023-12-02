# tinh diem trung binh
import math

class SinhVien:
    def __init__(self,id,name,d1,d2,d3) -> None:
        self.id="SV{:02d}".format(id)
        self.name=name
        self.d1=d1
        self.d2=d2
        self.d3=d3
        self.tb=math.ceil((d1*3+d2*3+d3*2)*100/8)/100

    def getTB(self):
        return self.tb

    def __str__(self) -> str:
        return f"{self.id} {self.name} {self.tb:.2f} {self.rank}"
    
a=[]
for i in range(int(input())):
    s=input().split()
    for j in range(len(s)):
        s[j]=s[j].title()
    name=" ".join(s)
    a.append(SinhVien(i+1,name,float(input()),float(input()),float(input())))

a.sort(key=lambda i: i.id)
a.sort(key=lambda i: i.tb,reverse=True)

res,tmp=1,a[0]
tmp.rank=1

for i in a:
    if i.tb<tmp.tb:
        i.rank=res
        tmp=i
    else: i.rank=tmp.rank
    print(i)
    res+=1


# 4
#  ha Thi kieu     anh
# 7
# 6
# 7
# Pham    THI  HAO
# 7
# 7
# 7
# dao manh ninh
# 7
# 7
# 7
# nguyen manh son
# 5
# 5
# 5