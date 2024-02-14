from pprint import pprint
def findLargestSquareSize(samples):
    n = len(samples)
    dp = [[0] * n for _ in range(n)]
    max_size = 0

    for i in range(n):
        for j in range(n):
            if samples[i][j] == 1:
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                max_size = max(max_size, dp[i][j])

    return max_size

print(findLargestSquareSize([[1, 1, 1], [1, 1, 0], [1, 0, 1]]))