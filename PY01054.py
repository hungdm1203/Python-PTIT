# tich chu so

for _ in range(int(input())):
    mul=1
    li=list(int(i) for i in input())
    for i in li:
        if i!=0:
            mul=mul*i
    print(mul)