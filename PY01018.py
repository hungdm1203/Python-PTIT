# ma hoa-2

P= "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
while True:
    str=input()
    if str=='0':
        break
    k,s=str.split()
    tmp=""
    for i in s:
        j=P.find(i)
        tmp=P[(j+int(k))%28]+tmp
    print(tmp)