# thu phi xe o to

def check(s,n):
    if "con" in s and n==5: return 10000
    if "con" in s and n==7: return 15000
    if "tai" in s and n==2: return 20000
    if "khach" in s and n==29: return 50000
    if "khach" in s and n==45: return 70000

a={}
for _ in range(int(input())):
    arr=input().split()
    if arr[-2]=="OUT": continue
    if arr[-1] in a: a[arr[-1]]=check(arr[1],int(arr[2]))+a[arr[-1]]
    else: a[arr[-1]]=check(arr[1],int(arr[2]))

for i in a:
    print(f"{i}: {a[i]}")
