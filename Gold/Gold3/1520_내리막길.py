import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(x, y):
    global result
    if x == N-1 and y == M-1:
        return 1

    if dp[x][y] != 1:
        dp[x][y] = 0

        for dx, dy in ((1, 0), (0, -1), (0, 1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] < arr[x][y]:
                dp[x][y] += dfs(nx, ny)

    return dp[x][y]

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [[-1] * M for _ in range(N)]

print(dfs(0, 0))