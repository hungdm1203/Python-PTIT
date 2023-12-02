# dien so

for _ in range(int(input())):
    n=int(input())
    a=set(int(i) for i in input().split())
    print(max(a)-min(a)+1-len(a))