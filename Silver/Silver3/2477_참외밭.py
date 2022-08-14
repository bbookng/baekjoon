import sys
input = sys.stdin.readline

K = int(input())
arr = [list(map(int, input().split()))for _ in range(6)]
max_C = max_R = c = r = 0

for i in range(6):
    if arr[i][0] < 3:
        if arr[i][1] > max_C:
            max_C = arr[i][1]
            c = arr[i-3][1] if i > 2 else arr[i+3][1]
    else:
        if arr[i][1] > max_R:
            max_R = arr[i][1]
            r = arr[i-3][1] if i > 2 else arr[i+3][1]


print((max_C * max_R - c * r) * K)