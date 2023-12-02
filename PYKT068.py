# danh sach mon thi


li=[]
for _ in range(int(input())):
    a=input()
    b=input()
    c=input()
    s=a+" "+b+" "+c
    li.append(s)
li.sort()
for i in li:
    print(i)