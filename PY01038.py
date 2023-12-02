# kiem tra chia het cho 7


def test(n):
    sum=n
    for i in range(1000):
        if(sum%7!=0):
            sum=sum+int(str(sum)[::-1])
        else:
            return sum
    return -1

for _ in range(int(input())):
    n=int(input())
    print(test(n))