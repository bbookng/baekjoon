import sys
input = sys.stdin.readline

N, M = map(int, input().split())
apps = list(map(int, input().split()))
costs = list(map(int, input().split()))

_max = sum(costs)
result = int(1e9)

dp = [[0] * _max for _ in range(N+1)]

for i in range(N):
    byte = apps[i]
    cost = costs[i]

    for j in range(_max):
        if j < cost:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j-cost] + byte, dp[i-1][j])
        if dp[i][j] >= M:
            result = min(result, j)

print(result)