# tong chu so

s=input()
tong=0
if s[0]=='-':
    s=s[1:]
    tong=-3
dem=0
while len(s)>1:
    tong += sum(int(i) for i in s)
    dem+=1
    s=str(tong)
    tong=0
print(dem)