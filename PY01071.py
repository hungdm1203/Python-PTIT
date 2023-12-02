# python file

s=input().lower()
if s[-3::1]=='.py' and len(s)>=3:
    print('yes')
else: print('no')