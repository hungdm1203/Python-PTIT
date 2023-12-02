# tinh diem thi ielts


def point(score):
    if score >= 39:
        return 9.0
    elif score >= 37:
        return 8.5
    elif score >= 35:
        return 8.0
    elif score >= 33:
        return 7.5
    elif score >= 30:
        return 7.0
    elif score >= 27:
        return 6.5
    elif score >= 23:
        return 6.0
    elif score >= 20:
        return 5.5
    elif score >= 16:
        return 5.0
    elif score >= 13:
        return 4.5
    elif score >= 10:
        return 4.0
    elif score >=7:
        return 3.5
    elif score >=5:
        return 3.0
    elif score >=3:
        return 2.5
    
    

for _ in range(int(input())):
    a=list(float(i) for i in input().split())
    a[0]=point(int(a[0]))
    a[1]=point(int(a[1]))
    
    
    diem=sum(a)/4.0
    if diem - int(diem) >= 0.75: 
        print(float(int(diem))+1.0)
    elif diem - int(diem) >= 0.25: 
        print(float(int(diem)+0.5))
    else: print(float(int(diem)))