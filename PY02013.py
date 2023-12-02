# bien doi ve 1

while True:
    n=int(input())
    if n==0:
        break
    se={n}
    while n!=1:
        if n%2==0:
            n=n/2
            se.add(n)
        else:
            n=n*3+1
            se.add(n)
    print(len(se))