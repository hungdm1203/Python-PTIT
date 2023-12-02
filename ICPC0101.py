# thu gon day so


n=int(input())
li=list(int(i) for i in input().split())
i=0
while i<len(li)-1:
    if (li[i]+li[i+1])%2==0:
        li.pop(i)
        li.pop(i)
        if i>=1:
            i=i-1
    else: i=i+1
print(len(li))


