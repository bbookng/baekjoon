import sys
input = sys.stdin.readline

def dfs(depth, idx):
    global min_V
    if depth == N // 2:
        start, link = 0, 0
        for i in range(N):
            for j in range(i + 1, N):
                if visited[i] and visited[j]:
                    start += (arr[i][j] + arr[j][i])
                elif not visited[i] and not visited[j]:
                    link += (arr[i][j] + arr[j][i])
        min_V = min(min_V, abs(start - link))
        return

    for i in range(idx, N):
        if not visited[i]:
            visited[i] = 1
            dfs(depth + 1, i + 1)
            visited[i] = 0



N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [0] * N
min_V = float('inf')

dfs(0, 0)
print(min_V)

