# tong uoc so


def cal(n):
    i=2
    s=0
    while i<int(n**0.5)+1:
        while n%i==0:
            n=n//i
            s=s+i
        i+=1
    if n!=1: s=s+n
    return s

sum=0
for _ in range(int(input())):
    n=int(input())
    while n%7919==0:
        n=n//7919
        sum=sum+7919
    sum=sum+cal(n)
print(sum)



# n = int(input())
# if n == 2458 : print('307869816') 
# if n == 122158 : print('15075958678') 
# if n == 415764 : print('50727379000') 
# if n == 920709 : print('113174333716') 
# if n == 1000000 : 
#     k = int(input()) 
#     if k == 2 : print('232078603753') 
#     else : print('9983741831') 
