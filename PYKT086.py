# chuyen doi nhi phan

file=open("C:\WORKSPACE\Python_ptit\DATA.in",'r')
t=int(file.readline())
for _ in range(t):
    n=int(file.readline())
    x=file.readline()
    m=int(x,2)
    if n==2: print(bin(m)[2:])
    elif n==8: print(oct(m)[2:])
    elif n==16: print(hex(m)[2:])
    else:
        s=""
        while m>0:
            s=str(m%4) + s
            m=m//4
        print(s)
 