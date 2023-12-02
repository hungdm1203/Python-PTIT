# doi co so-2


for _ in range(int(input())):
    b=int(input())
    s=input()
    n=int(s,2)
    kq=''
    while n>0:
        n,a=divmod(n,b) #n=n//b a=n%b 
        if a<10:
            kq=str(a)+kq
        else: kq=chr(65+a-10)+kq
    print(kq)