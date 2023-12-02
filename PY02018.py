# so nho nhat con thieu

n=int(input())
li=list(int(i) for i in input().split())
li.sort()
for i in range(1,n+2):
    if i not in li:
        print(i)
        break