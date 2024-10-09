# 1407
A, B = map(int, input().split())

def calc(number):
    if number == 0:
        return 0
    elif number == 1:
        return  1
    elif number % 2 == 0:
        return number // 2 + 2 * calc(number // 2)
    elif number % 2 == 1:
        return number // 2 + 2 * calc(number // 2) + 1

print(calc(B) - calc(A-1))

# 2247