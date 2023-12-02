# so dac biet

mod = 1000000007
def pow(a, b):
    if b==1: return a
    if b&1: return pow(a, b-1)*a%mod
    p = pow(a, b>>1)
    return p*p%mod
def cal(n, k):
    if k<=1: return k
    ex = 0
    while (k>>ex)^1: ex+=1
    return pow(n, ex) + cal(n, k^(1<<ex))
for t in range(int(input())):
    n, k = map(int, input().split())
    print(cal(n, k)%mod)