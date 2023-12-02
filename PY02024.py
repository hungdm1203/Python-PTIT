# sap xep theo tich chu so

def build(s):
    tmp=1
    for i in s:
        tmp*=int(i)
    return tmp


for _ in range(int(input())):
    n=input()
    li=list(input().split())
    li.sort(key=lambda a: (build(a),int(a)))
    print(*li)
