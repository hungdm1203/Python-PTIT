# sap xep theo tong chu so



for _ in range(int(input())):
    n=int(input())
    li=[i for i in input().split()]
    li.sort(key=lambda a: (sum(int(j) for j in a),int(a)))
    print(*li)