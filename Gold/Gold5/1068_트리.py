import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
K = int(input())

def dfs(now):
    arr[now] = -2
    for i in range(N):
        if now == arr[i]:
            dfs(i)

cnt = 0
dfs(K)
for i in range(N):
    if arr[i] != -2 and i not in arr:
        cnt += 1

print(cnt)