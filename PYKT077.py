# lich thi hoc ky

from datetime import datetime
class Mon:
    def __init__(self, code, name) -> None:
        self.code = code
        self.name = name

class CaThi(Mon):
    def __init__(self, i, m, arr) -> None:
        self.code = 'T{:03d}'.format(i)
        self.m = m
        self.date = datetime.strptime(arr[1], '%d/%m/%Y')
        self.strdate = arr[1]
        self.time = datetime.strptime(arr[2], '%H:%M')
        self.strtime = arr[2]
        self.group = arr[3]

    def __str__(self) -> str:
        return f"{self.code} {self.m.code} {self.m.name} {self.strdate} {self.strtime} {self.group}"

n, m = map(int, input().split())
a, arr = {}, []
for _ in range(n):
    s = input()
    a[s] = Mon(s, input())
    
for i in range(m):
    li = input().split()
    arr.append(CaThi(i+1, a[li[0]], li))

arr.sort(key=lambda x:(x.date,x.time,x.m.code))
for i in arr: print(i)

