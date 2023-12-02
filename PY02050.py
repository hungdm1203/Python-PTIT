# doan lien tiep nho hon

for _ in range(int(input())):
    n=input()
    li=list(int(i) for i in input().split())
    a=[]
    for i in range(len(li)):
        while len(a)>0 and li[i]>=li[a[len(a)-1]]:
            a.pop(len(a)-1)
        if len(a)==0:
            print(i+1,end=' ')
        else: print(i-a[len(a)-1],end=" ")
        a.append(i)
    print()