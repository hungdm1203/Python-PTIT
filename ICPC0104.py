# tim so nho nhat


for _ in range(int(input())):
    s=input()
    res=""
    mi=float('inf')
    for i in s:
        if i.isdigit():
            res=res+i
        else:
            if res!="":
                mi=min(mi,int(res))
            res=""
    if res!="":
        print(min(mi,int(res)))
    else: print(mi)
