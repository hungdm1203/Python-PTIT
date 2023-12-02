# chu hoa-chu thuong

s=input()
if sum(1 for i in s if i.isupper())>sum(1 for i in s if i.islower()):
    print(s.upper())
else: print(s.lower())