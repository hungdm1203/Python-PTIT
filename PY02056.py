# so thuan nghich lon nhat trong ma tran

def check(n):
    s=str(n)
    return s==s[::-1] and n>=10

n,m=map(int,input().split())
a=[]
ma=0
for _ in range(n):
    li=[int(i) for i in input().split()]
    a.append(li)
    for i in li:
        if check(i): ma=max(ma,i)

if ma==0:
    print("NOT FOUND")
else:
    print(ma)
    for i in range(n):
        for j in range(m):
            if a[i][j]==ma:
                print(f"Vi tri [{i}][{j}]")
