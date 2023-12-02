# so may man-2

for _ in range(int(input())):
    n=input()
    if all(int(i)==4 or int(i)==7 for i in n):
        print('YES')
    else: print('NO')