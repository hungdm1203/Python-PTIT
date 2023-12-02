# sum triple zero


# from itertools import combinations
# for _ in range(int(input())):
#     n=int(input())
#     li=list(int(i) for i in input().split())
#     a=list(combinations(li,3))
#     dem=0
#     for i in a:
#         if sum(i)==0:
#             dem=dem+1
#     print(dem)

for _ in range(int(input())):
    n=int(input())
    li=list(int(i) for i in input().split())
    li.sort()
    dem=0
    for i in range(len(li)-2):
        l=i+1
        r=n-1
        while l<r: 
            tmp=li[i]+li[l]+li[r]
            if tmp==0:
                dem+=1
                l+=1
            elif tmp<0:
                l+=1
            else: r-=1
    print(dem)

    