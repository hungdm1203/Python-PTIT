# lai suat ngan hang

import math
for _ in range(int(input())):
    a,b,c=map(float,input().split())
    print(int(math.log(c/a,1+b/100))+1)