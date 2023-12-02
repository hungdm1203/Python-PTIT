# sap dat lai xau ky tu

for i in range(int(input())):
    a=list(i for i in input())
    b=list(i for i in input())
    a.sort()
    b.sort()
    if a==b:
        print(f"Test {i+1}: YES")
    else: print(f"Test {i+1}: NO")
