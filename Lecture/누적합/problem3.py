# 2304, 14719

N = int(input())
dp = [0] * 1001

for _ in range(N):
    a, b = map(int, input().split())
    dp[a] = b

for i in range(dp.index(max(dp))):
    if dp[i] > dp[i + 1]:
        dp[i + 1]  = dp[i]

for j in range(1000, dp.index(max(dp)), -1):
    if dp[j] > dp[j - 1]:
        dp[j - 1] = dp[j]

print(sum(dp))
