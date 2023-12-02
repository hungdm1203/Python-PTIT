# lon nhat va nho nhat


while True:
    n=int(input())
    if n==0:
        break
    li=[]
    for i in range(n):
        x=int(input())
        li.append(x)
    mi=min(li)
    ma=max(li)
    if mi!=ma:
        print(f"{mi} {ma}")
    else:
        print("BANG NHAU")