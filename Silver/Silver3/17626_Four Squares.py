import sys
import math
input = sys.stdin.readline

N = int(input())

cnt = 1
while N % math.sqrt(N):
    N = round(math.sqrt(N))
    N //= math.sqrt(N)
    cnt += 1

print(cnt)