import sys
input = sys.stdin.readline

N = int(input())

numbers = [0] * 10

std = 1

while N != 0:
    while N % 10 != 9:
        for i in str(N):
            numbers[int(i)] += std
        N -= 1

    if N < 10:
        for i in range(N + 1):
            numbers[i] += std
        numbers[0] -= std
        break
    else:
        for i in range(10):
            numbers[i] += ( N // 10 + 1) * std

    numbers[0] -= std
    std *= 10
    N //= 10

for i in numbers:
    print(i, end=' ')