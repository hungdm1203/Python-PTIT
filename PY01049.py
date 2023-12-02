# chu so nguyen to

import math
def nto(n):
    return n > 1 and all(n%i!=0 for i in range(2,int(n**0.5)+1))


for _ in range(int(input())):
    n=input()
    dem=0
    for i in n:
        if(nto(int(i))):
            dem+=1
    if nto(len(n)) and dem>len(n)-dem:
        print("YES")
    else: print("NO") 


