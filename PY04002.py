# lop rectangle

class Rectangle:
    def __init__(self,length,width,col):
        self.length=length
        self.width=width
        self.col=col.title()

    def perimeter(self):
        return (self.length+self.width)*2
    
    def area(self):
        return self.length*self.width
    
    def color(self):
        return self.col.title()
    
arr = input().split()
if int(arr[0])>0 and int(arr[1])>0:
    r = Rectangle(int(arr[0]), int(arr[1]), arr[2])
    print('{} {} {}'.format(r.perimeter(), r.area(), r.color()))
else: print("INVALID")