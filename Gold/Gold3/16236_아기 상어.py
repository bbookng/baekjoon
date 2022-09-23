import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

size = 2

for i in range(N):
    for j in range(N):
        if board[i][j] == 9:
            board[i][j] = 0
            a, b = i, j
            break

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

fish = []
cnt = 0

def bfs():
    visited = [[-1] * N for _ in range(N)]
    q = deque([(a, b, 0)])
    visited[a][b] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == -1 and board[nx][ny] <= size:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny, visited[nx][ny] + 1))
                fish.append((nx, ny, visited[nx][ny] + 1))

    if len(fish) > 0:


