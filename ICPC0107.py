# thay doi chu so


for _ in range(int(input())):
    a,b=input().split()
    ip = input().split()
    if len(ip) == 1:
        x = ip[0]
        y = input()
    else:
        x, y = ip
    n1=int(x.replace(a,b))+int(y.replace(a,b))
    n2=int(x.replace(b,a))+int(y.replace(b,a))
    print(f"{min(n1,n2)} {max(n1,n2)}")
