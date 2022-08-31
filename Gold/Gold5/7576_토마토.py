import sys
input = lambda :sys.stdin.readline().strip()
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 0:
                board[nx][ny] = board[x][y] + 1
                q.append((nx, ny))


M, N = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
q = deque([])

for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            q.append((i, j))


bfs()

result = 0

for i in board:
    if i.count(0) > 0:
        print(-1)
        exit()
    else:
        result = max(result, max(i))

print(result-1)