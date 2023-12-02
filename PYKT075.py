# sao chep danh ba

def getName(s):
    li=s.split()
    for i in range(len(li)):
        li[i]=li[i].title()
    return " ".join(li)

class Info:
    def __init__(self,name,phone,date) -> None:
        self.name=name
        self.phone=phone
        self.date=date
        self.ten=name.split()[-1]
        self.ho=name.split()[:-1]

    def __str__(self) -> str:
        return f"{self.name}: {self.phone} {self.date}"

ip=open('SOTAY.txt','r')

a=[]
line=[i.strip() for i in ip if i.strip()!=""]
date=line[0].split()[1]
i=1
while i<len(line):
    s=line[i]
    i+=1
    if "/" in s:
        date=s.split()[1]
        continue
    tmp=line[i]
    i+=1
    a.append(Info(getName(s),tmp,date))

a.sort(key=lambda i:(i.ten,i.ho))

for i in a: print(i)