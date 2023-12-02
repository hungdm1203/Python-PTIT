# so phan nguyen to nho nhat



# def uoc(n):
#     uoc=list(i for i in range(1,n+1) if n%i==0)
#     return len(uoc)


# def test(n):
#     uocMax=max(li[0:n+1])
#     for i in range(n,2*n):
#         if li[i]>uocMax or (li[i]==uocMax and i==n and li[0:n+1].count(uocMax)==1):
#             print(i)
#             break

# a=[]
# for _ in range(int(input())):
#     a.append(int(input()))
# aMax=max(a)
# li=[0]
# for i in range(1,2*aMax+1):
#     li.append(uoc(i))


# for i in a:
#     test(i)


a = [1, 2, 4, 6, 12, 24, 36, 48, 60, 120, 180, 240, 360, 720, 840, 1260, 1680, 2520, 5040, 7560, 10080, 15120, 20160, 25200, 27720, 45360, 50400, 55440, 83160, 110880, 166320, 221760, 277200, 332640, 498960, 554400, 665280, 720720, 1081080, 1441440, 2162160, 2882880, 3603600, 4324320, 6486480, 7207200, 8648640, 10810800]
for _ in range(int(input())):
    n=int (input())
    for i in a:
        if i>=n:
            print(i)
            break