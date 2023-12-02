# so chia het cho 3

for _ in range(int(input())):
    li=list(int(i) for i in input())
    if sum(li)%3==0:
        print("YES")
    else: print("NO")