import sys
input = sys.stdin.readline
from collections import deque

def bfs(si, sj):
    visited = [[0] * M for _ in range(N)]
    q = deque()
    q.append((si, sj))
    visited[si][sj] = 0
    while q:
        ci, cj = q.popleft()
        for di, dj in ((-1, 0), (1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0:
                q.append((ni, nj))
                visited[ni][nj] = visited[ci][cj] + 1
                if arr[ni][nj] == 1:
                    return visited[ni][nj]





N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

result = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            result = max(result, bfs(i, j))
print(result)
