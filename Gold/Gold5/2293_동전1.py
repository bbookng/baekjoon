import sys
input = sys.stdin.readline

# N : 동전의 가짓수
# K : 가치의 합

N, K = map(int, input().split())

dp = [0] * (K+1)
dp[0] = 1
coins = [int(input()) for _ in range(N)]

for coin in coins:
    for i in range(coin, K+1):
        dp[i] += dp[i - coin]

print(dp[K])

