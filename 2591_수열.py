import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

result = 1
up = 1
down = 1

for i in range(n-1):
    if arr[i] <= arr[i + 1]:
        up += 1
        if up > result:
            result = up
        else:
            result
    else:
        up = 1

for j in range(n-1):
    if arr[j] >= arr[j + 1]:
        down += 1
        if down > result:
            result = down
        else:
            result
    else:
        down = 1

print(result)