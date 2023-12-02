# lop thi sinh 1

class ThiSinh:
    def __init__(self,name,dob,g1,g2,g3) -> None:
        self.name=name
        self.dob=dob
        self.g1=g1
        self.g2=g2
        self.g3=g3

    def __str__(self) -> str:
        return f"{self.name} {self.dob} {self.g1+self.g2+self.g3:.1f}"
    

ts=ThiSinh(input(),input(),float(input()),float(input()),float(input()))
print(ts.__str__())