import sys
input = sys.stdin.readline

INF = float('inf')
def solution():
    dp = [INF] * 100001

    for i in range(N+1):
        dp[i] = N-i

    for i in range(N+1, K+1):
        if i % 2:
            dp[i] = min(dp[i-1]+1, dp[(i+1)//2]+1)
        else:
            dp[i] = min(dp[i-1]+1, dp[i//2])

    return dp[K]

N, K = map(int, input().split())

print(solution())