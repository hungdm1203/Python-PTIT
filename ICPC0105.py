# tim so lon nhat


for _ in range(int(input())):
    s=input()
    res=""
    ma=0
    for i in s:
        if i.isdigit():
            res=res+i
        else:
            if res!="":
                ma=max(ma,int(res))
            res=""
    if res!="":
        print(max(ma,int(res)))
    else: print(ma)
