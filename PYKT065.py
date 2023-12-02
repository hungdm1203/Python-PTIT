# kiem tra chia het


def test(i,n):
    for j in range(2,n+1):
        if i%j==0:
            return 0
    return 1



while True:
    line = input()
    if line[:2] == '-1':
        break
    a, b = map(int, line.split())
    n = int(input())


    dem=0
    for i in range(a,b+1):
        if test(i,n)==1:
            dem+=1
    print(dem)


