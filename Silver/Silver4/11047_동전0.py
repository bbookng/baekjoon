import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]

cnt = 0
for i in reversed(arr):
    cnt += K // i
    K %= i
print(cnt)
