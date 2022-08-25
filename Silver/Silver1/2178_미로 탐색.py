import sys
from collections import deque
input = lambda :sys.stdin.readline().strip()

def bfs(x, y):
    visited = [[-1]*M for _ in range(N)]
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        if x == N-1 and y == M-1:
            return visited[N-1][M-1]
        for dx, dy in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
            nx, ny = x+dx, y+dy
            if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 1 and visited[nx][ny] == -1:
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1


N, M = map(int, input().split())
board = [list(map(int, input())) for _ in range(N)]

print(bfs(0, 0))
