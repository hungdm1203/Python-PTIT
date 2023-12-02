# bang xep hang

class SinhVien:
    def __init__(self,name,ac,sub) -> None:
        self.name=name
        self.sub=sub
        self.ac=ac
    def __str__(self) -> str:
        return f"{self.name} {self.ac} {self.sub}"
    
a=[]
for _ in range(int(input())):
    s=input()
    ac,sub=map(int,input().split())
    a.append(SinhVien(s,ac,sub))

a.sort(key=lambda i:(-i.ac,i.sub,i.name))
for i in a: print(i)

