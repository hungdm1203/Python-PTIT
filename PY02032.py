# liet ke cac so co hai chu so tang dan

s=input()
a=[]
for i in range(0,len(s),2):
    if int(s[i:i+2]) not in a and int(s[i:i+2])>=10:
        a.append(int(s[i:i+2]))
# a.sort()
print(*a)