import sys
input = sys.stdin.readline

arr = [list(map(int, input().split())) for i in range(5)]
ans = [list(map(int, input().split())) for i in range(5)]

cnt = 0
for i in ans:
    for j in arr:
        for k in j:
            if i == k:
                k = 0
                cnt += 1


print(arr)