year = int(input())

# 윤년 = 4의 배수, 100의배수가 아닐 때, 400의 배수일 때

if year % 4 == 0:
    if year % 400 == 0:
        print(1)
    elif year % 100 != 0:
        print(1)
    elif year % 100 == 0:
        print(0)

else:
    print(0)

