# 1978
import sys

n = int(sys.stdin.readline())
arr = map(int, sys.stdin.readline().split())

result = 0

for i in arr:
    cnt = 0
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                cnt += 1
        if cnt == 0:
            result += 1

print(result)

# 11653
N = int(input())
number = 2

while N != 1:
    if N % number == 0:
        print(number)
        N //= number
    else:
        number += 1

# 14232
from math import ceil, sqrt

N = int(input())
answer = []

for i in range(2, ceil(sqrt(N)) + 1):
    if N % i == 0:
        answer.append(i)
        N //= i

if N != 1:
    answer.append(N)

print(len(answer))
print(*sorted(answer))
