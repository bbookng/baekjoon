import sys
input = lambda : sys.stdin.readline().strip()

dp = [0] * 1001
n = int(input())
for i in range(n):
    a, b = map(int,input().split())
    dp[a] = b

for i in range(dp.index(max(dp))):
    if dp[i] > dp[i + 1]:
        dp[i+1] = dp[i]

height = 0
for i in range(1000, dp.index(max(dp)), -1):
    if dp[i] > dp[i-1]:
        dp[i-1] = dp[i]

print(sum(dp))


