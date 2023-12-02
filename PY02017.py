# tan suat le
import collections

for _ in range(int(input())):
    n=int(input())
    a=[int(i) for i in input().split()]
    res=collections.Counter(a).most_common()
    for i in res: 
        if i[1]%2!=0:
            print(i[0])
            break
