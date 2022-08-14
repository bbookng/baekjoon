import sys
input = sys.stdin.readline

K = int(input())
arr = [list(map(int, input().split()))for _ in range(6)]
max_C = max_R = 0

for i in arr:
    if i[0] < 3:
        if i[1] > max_C:
            max_C = i[1]
    else:
        if i[1] > max_R:
            max_R = i[1]



print((max_C * max_R - minus) * K)