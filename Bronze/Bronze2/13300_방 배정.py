import sys

input = lambda: sys.stdin.readline().strip()

n, k = map(int, input().split())

cnt = 0
arr = [[0] * 6 for _ in range(2)]

for _ in range(n):
    x, y = map(int,input().split())
    arr[x][y-1] += 1

result = 0
for i in range(2):
    for j in range(6):
        result += (arr[i][j] + k - 1) // k

print(result)