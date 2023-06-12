import sys
from collections import deque
input = sys.stdin.readline

def solution(i, j):
    q = deque([(i, j)])
    visited[i][j] = 0

    while q:
        x, y = q.popleft()

        for dx, dy in ((-1, 0), (1, 0), (0, 1), (0, -1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == -1:
                if not board[nx][ny]:
                    visited[nx][ny] = 0
                elif board[nx][ny] == 1:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[-1] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if board[i][j] == 2 and visited[i][j] == -1:
            solution(i, j)
            break

for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            print(0, end=' ')
        else:
            print(visited[i][j], end=' ')
    print()
