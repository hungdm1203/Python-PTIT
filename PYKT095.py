# tinh tien dien

class Guest:
    def __init__(self,id,name,type,old,new) -> None:
        self.id="KH{:02d}".format(id)
        self.name=name
        self.old=old
        self.new=new
        self.type=type
        if self.type=="A":
            if new-old<100:
                self.inn=(new-old)*450
                self.out=0
                self.vat=0
                self.sum=self.inn
            else:
                self.inn=100*450
                self.out=(new-old-100)*1000
                self.vat=int(self.out*5/100)
                self.sum=self.inn+self.out+self.vat
        elif self.type=="B":
            if new-old<500:
                self.inn=(new-old)*450
                self.out=0
                self.vat=0
                self.sum=self.inn
            else:
                self.inn=500*450
                self.out=(new-old-500)*1000
                self.vat=int(self.out*5/100)
                self.sum=self.inn+self.out+self.vat
        else:
            if new-old<200:
                self.inn=(new-old)*450
                self.out=0
                self.vat=0
                self.sum=self.inn
            else:
                self.inn=200*450
                self.out=(new-old-200)*1000
                self.vat=int(self.out*5/100)
                self.sum=self.inn+self.out+self.vat


    def __str__(self) -> str:
        return f"{self.id} {self.name} {self.inn} {self.out} {self.vat} {self.sum}" 
    

a=[]
for i in range(int(input())):
    name=input().split()
    arr=input().split()
    for j in range(len(name)):
        name[j]=name[j].title()
    res=" ".join(name)

    a.append(Guest(i+1,res,arr[0],int(arr[1]),int(arr[2])))

a.sort(key=lambda i:i.sum,reverse=True)
for i in a:print(i)