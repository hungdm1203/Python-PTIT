# so xen ke

for _ in range(int(input())):
    li=list(i for i in input())
    if len(li)%2!=0 and li[0]!=li[1] and all(li[i]==li[0] for i in range(0,len(li),2)):
        print("YES")
    else: print("NO")