# 문제 1. 비밀번호 (# 1816)

T = int(input())

for _ in range(T):
    number = int(input())

    for i in range(2, 1000001):
        if number % i == 0:
            print("NO")
            break
    else:
        print("YES")
