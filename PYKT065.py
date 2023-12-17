# kiem tra chia het

while True:
    line = input()
    if len(line)==2:
        break
    a, b = map(int, line.split())
    n = int(input())

    arr=[1]*(b+1)
    for i in range(a,len(arr)):
        if arr[i]!=0:
            for j in range(2,n+1):
                if i%j==0: 
                    arr[i]=0
                    break
        else:
            for j in range(i,len(arr),i):
                arr[j]=0

    print(sum(arr[a:]))