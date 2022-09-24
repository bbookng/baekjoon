import sys
input = sys.stdin.readline

N = int(input())

max_dp = [0, 0, 0]
min_dp = [0, 0, 0]

for i in range(N):
    a, b, c = map(int, input().split())
    for j in range(3):
        if j == 0:
            max_tmp1 = max(max_dp[j], max_dp[j+1]) + a
            min_tmp1 = min(min_dp[j], min_dp[j+1]) + a
        elif j == 1:
            max_tmp2 = max(max_dp[j-1], max_dp[j], max_dp[j+1]) + b
            min_tmp2 = min(min_dp[j-1], min_dp[j], min_dp[j+1]) + b
        elif j == 2:
            max_tmp3 = max(max_dp[j-1], max_dp[j]) + c
            min_tmp3 = min(min_dp[j-1], min_dp[j]) + c

    max_dp = [max_tmp1, max_tmp2, max_tmp3]
    min_dp = [min_tmp1, min_tmp2, min_tmp3]

print(max(max_dp), min(min_dp))




