# chen dau phay


li=list(i for i in input())
for i in range(len(li)-3,0,-3):
    li.insert(i,",")
print("".join(li))
