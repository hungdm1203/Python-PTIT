# xu li van ban

s=""
while True:
    try:
        s += input()
    except EOFError:
        break

li=[]
tmp=0
for i in range(len(s)):
    if s[i]=='.'or s[i]=='!' or s[i]=='?':
        li.append(s[tmp:i])
        tmp=i+1

for i in li:
    a=list(i.lower().split())
    a[0]=a[0].title()
    print(*a)
    

