# ma hoa 3

a="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for _ in range(int(input())):
    s=input()
    s1=s[:len(s)//2]
    s2=s[len(s)//2:]
    t1=t2=0
    for i in range(len(s1)):
        t1=t1+a.index(s1[i])
        t2=t2+a.index(s2[i])
    
    res1=res2=""
    for i in range(len(s1)):
        res1=res1+a[(a.index(s1[i])+t1)%26]
        res2=res2+a[(a.index(s2[i])+t2)%26]
    
    s=""
    for i in range(len(s1)):
        s=s+a[(a.index(res1[i])+a.index(res2[i]))%26]
    print(s)
