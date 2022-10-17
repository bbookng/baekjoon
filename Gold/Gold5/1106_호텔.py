C, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

arr.sort(key=lambda x:x[0])
dp = [0] + [float('inf')] * (C+100)
result = float('inf')

for cost, customer in arr:
    for i in range(customer, len(dp)):
        dp[i] = min(dp[i-customer] + cost, dp[i])
        if i >= C:
            result = min(dp[i], result)

print(result)

