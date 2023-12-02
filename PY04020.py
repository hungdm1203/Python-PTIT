# lap hoa don-3

class HoaDon:
    def __init__(self,id,name,quantity,price,discount) -> None:
        self.id=id
        self.name=name
        self.quantity=quantity
        self.price=price
        self.discount=discount
        self.sum=self.quantity*self.price-self.discount
    
    def __str__(self) -> str:
        return f"{self.id} {self.name} {self.quantity} {self.price} {self.discount} {self.sum}"
    

a=[]
for _ in range(int(input())):
    hd=HoaDon(input(),input(),int(input()),int(input()),int(input()))
    a.append(hd)

a.sort(key=lambda i:i.sum,reverse= True)
for i in a: print(i)