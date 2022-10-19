import sys
input = lambda: sys.stdin.readline().strip()
from collections import deque

def bfs(x, y):

    q = deque()
    q.append((x, y))
    cnt = 1
    tmp = []

    while q:
        x, y = q.popleft()
        for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M:
                if not visited[nx][ny] and not arr[nx][ny]:
                    cnt += 1
                    visited[nx][ny] = 1
                    q.append((nx, ny))
                else:
                    tmp.append((nx, ny))

    for i, j in tmp:
        visited[i][j] = 0
        answer[i][j] += cnt
        if answer[i][j] >= 10:
            answer[i][j] %= 10

N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
answer = [[0] * M for _ in range(N)]
visited = [[0] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            answer[i][j] = 1

for i in range(N):
    for j in range(M):
        if arr[i][j] == 0 and visited[i][j] == 0:
            visited[i][j] = 1
            bfs(i, j)


for i in range(N):
    print(''.join(map(str, answer[i])))

