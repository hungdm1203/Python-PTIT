# trung thuong


import collections


def check(a):
    tmp=max(collections.Counter.values(a))
    li=[]
    for i,j in collections.Counter.items(a):
        if j==tmp:
            li.append(i)
    return min(li)


for _ in range(int(input())):
    li=[]
    for _ in range(int(input())):
        li.append(int(input()))
    li.sort()
    a=collections.Counter(li)
    print(check(a))
