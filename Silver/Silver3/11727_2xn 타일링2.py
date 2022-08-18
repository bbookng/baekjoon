import sys
input = sys.stdin.readline

N = int(input())

dp =[0] * (N+1)
dp[1] = 1
for i in range(2, N+1):
    dp[i] = dp[i-1] * 2 + 1 if i % 2 == 0 else dp[i-1] * 2 - 1

print(dp[N] % 10007)


