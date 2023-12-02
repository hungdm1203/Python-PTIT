# chuan hoa cau

s=""
while True:
    try:
        s+=input()
        if s[-1] not in ".!?": s+="."
    except:
        break

a=[]
tmp=0

for i in range(len(s)):
    if s[i] in ".!?":
        a.append(s[tmp:i+1])
        tmp=i+1

for i in a:
    li=i.lower().split()
    li[0]=li[0].title()
    if li[-1]=="." or li[-1]=="?" or li[-1]=="!":
        print(" ".join(li[:-1])+li[-1])
    else: print(*li)

