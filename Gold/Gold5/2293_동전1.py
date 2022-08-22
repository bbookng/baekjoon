import sys
input = sys.stdin.readline

N, K = map(int, input().split())

dp = [0] * (K+1)
coins = [int(input()) for _ in range(N)]

for coin in coins:
    dp[coin] = 1

for i in range(1, K+1):
    for





print(min(dp))
