# so co 9 uoc so


def check(n):
    uoc=0
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            uoc+=2
            if n/i==i:
                uoc=uoc-1
        if uoc>9:
            return 0
    if uoc==9:
        return 1
    else: return 0
    


n=int(input())
dem=0
for i in range(1,n+1):
    if check(i)==1:
        dem=dem+1

print(dem)