# tach doi va tinh tong

s=input()
while len(s)>1:
    a=int(s[:len(s)//2])
    b=int(s[len(s)//2:])
    s=str(a+b)
    print(s)