import sys
input = sys.stdin.readline

N = int(input())

dp =[0] * (N+1)

for i in range(1, N+1):
    if i == 1:
        dp[i] = 1
    elif i == 2:
        dp[i] = 2
    else:
        dp[i] = dp[i-2] + dp[i-1]

print(dp[N] % 10007)

'''
import sys
input = sys.stdin.readline

N = int(input())

dp =[0] * (N+2)
dp[1] = 1
dp[2] = 2

for i in range(3, N+1):
    dp[i] = dp[i-2] + dp[i-1]

print(dp[N] % 10007)
'''