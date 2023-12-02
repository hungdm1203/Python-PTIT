# lap hoa don 1


class KhachHang:
    tien=0
    def __init__(self,id,name,old,new) -> None:
        self.id='KH{:02d}'.format(id)
        self.name=name
        self.old=old
        self.new=new
        self.tien=self.tinhtien()

    def tinhtien(self):
        if self.new-self.old<=50:
            return round(100*(self.new-self.old)*1.02)
        elif self.new-self.old<=100:
            sotien=150*(self.new-self.old-50)+100*50
            return round(sotien*1.03)
        else: 
            sotien=100*50+150*50+200*(self.new-self.old-100)
            return round(sotien*1.05)

    def __str__(self) -> str:
        return f"{self.id} {self.name} {self.tien}"



a=[]
for i in range(int(input())):
    kh=KhachHang(i+1,input(),int(input()),int(input()))
    a.append(kh)


a.sort(key=lambda i: i.tien,reverse=True)
for i in a:
    print(i.__str__())
    