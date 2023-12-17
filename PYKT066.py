# day con ngan nhat


import math
for _ in range(int(input())):
    n,k=map(int,input().split())
    li=[]
    while len(li)<n:
        li+=[int(i) for i in input().split()]
    res=n+1
    for i in range(n):
        tmp=li[i]
        if tmp%k==0:
            for j in range(i,n):
                if math.gcd(tmp,li[j])==k:
                    res=min(res,j-i+1)
                elif math.gcd(tmp,li[j])<k:
                    break 
                    
        

    if res!=n+1:
        print(res)
    else: print(-1)# day con ngan nhat


import math
for _ in range(int(input())):
    n,k=map(int,input().split())
    li=[]
    while len(li)<n:
        li+=[int(i) for i in input().split()]
    res=n+1
    for i in range(n):
        tmp=li[i]
        if tmp%k==0:
            for j in range(i,n):
                if math.gcd(tmp,li[j])==k:
                    res=min(res,j-i+1)
                elif math.gcd(tmp,li[j])<k:
                    break 
                    
        

    if res!=n+1:
        print(res)
    else: print(-1)