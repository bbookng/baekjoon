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