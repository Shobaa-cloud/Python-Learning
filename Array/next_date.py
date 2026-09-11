# Find the next date for a given day
# Input format: DD/MM/YYYY
# Leap year logic is handled

s=input().split("/")

d,m,y=map(int,s)

if y%400==0 or (y%100!=0 and y%4==0):
    if m==2:
        if d==28:
            d=29
        elif d==29:
            d=1
            m=3
        else:
            d+=1
        print(f'{d:02d}/{m:02d}/{y}')

    elif m in [4,6,9,11]:
        if d==30:
            d=1
            m+=1
        else:
            d+=1
        print(f'{d:02d}/{m:02d}/{y}')

    else:
        if d==31:
            d=1
            m+=1
            if m==13:
                m=1
                y+=1
        else:
            d+=1
        print(f'{d:02d}/{m:02d}/{y}')

else:
    if m==2:
        if d==28:
            d=1
            m+=1
        else:
            d+=1
        print(f'{d:02d}/{m:02d}/{y}')

    elif m in [4,6,9,11]:
        if d==30:
            d=1
            m+=1
        else:
            d+=1
        print(f'{d:02d}/{m:02d}/{y}')

    else:
        if d==31:
            d=1
            m+=1
            if m==13:
                m=1
                y+=1
        else:
            d+=1
        print(f'{d:02d}/{m:02d}/{y}')