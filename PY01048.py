# tong lien tiep

for _ in range(int(input())):
    n=int(input())
    res=0
    a=[i for i in range(0,n+1)]
    for i in range(1,int(n/2)+1):
        for j in range(i+1,n):
            if sum(a[i:j+1])==n:
                res+=1
            if sum(a[i:j+1])>=n:
                break
    print(res)