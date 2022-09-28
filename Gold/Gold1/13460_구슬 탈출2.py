import sys
input = lambda :sys.stdin.readline().strip()
from collections import deque

dx = [-1, 1, 0, 0]
dy = [1, 1, 0, -1]

def bfs():
    q = deque()
    visited = [[0] * M for _ in range(N)]
    q.append(Red)
    i = 0
    while q:
        x, y = q.popleft()
        while True:
            nx, ny = x + dx[i], y + dy[i]
            print(nx, ny)
            if 0 <= nx < N and 0 <= ny < M:
                if arr[nx][ny] == '#':
                    while arr[nx][ny] != '#':
                        i += 1
                        if i > 3:
                            i -= 4

                elif arr[nx][ny] == 'O':
                    return visited[nx][ny]
                visited[nx][ny] = 1
                q.append((nx, ny))


N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]

for i in range(N):
    for j in range(M):
        if arr[i][j] == 'R':
            Red = (i, j)
        elif arr[i][j] == 'B':
            Blue = (i, j)
        elif arr[i][j] == 'O':
            hole = (i, j)

print(bfs())