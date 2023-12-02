# tinh toan luong mua


class TramDo:
    def __init__(self,id,name,times,pmm) -> None:
        self.id=id
        self.name=name
        self.times=times
        self.pmm=pmm

    def __str__(self) -> str:
        return f"{self.id} {self.name} {self.pmm*60.0/self.times:.2f}"
    


dem=1
li=[]
a=[]
for _ in range(int(input())):
    name=input()
    start=[int(i) for i in input().split(':')]
    end=[int(i) for i in input().split(':')]
    pmm=float(input())
    
    times=end[0]*60+end[1]-start[0]*60-start[1]
    
    if name not in li:
        li.append(name)
        id=''
        if dem<10:
            id="T0"+str(dem)
        else: id="T"+str(dem)
        tram=TramDo(id,name,times,pmm)
        dem+=1
        a.append(tram)
    else:
        ind=li.index(name)
        a[ind].times=a[ind].times+times
        a[ind].pmm=a[ind].pmm+pmm


for i in a:
    print(i.__str__())
