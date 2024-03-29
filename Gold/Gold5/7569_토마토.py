import sys
from collections import deque
input = lambda :sys.stdin.readline().strip()

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

def bfs():
    while q:
        x, y, z = q.popleft()

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0 <= nx < N and 0 <= ny < M and 0 <= nz < H and board[nz][nx][ny] == 0:
                q.append((nx, ny, nz))
                board[nz][nx][ny] = board[z][x][y] + 1



M, N, H = map(int, input().split())
board = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
q = deque([])

for i in range(H):
    for j in range(N):
        for k in range(M):
            if board[i][j][k] == 1:
                q.append((j, k, i))

bfs()

result = 0

for i in board:
    for j in i:
        if j.count(0) > 0:
            print(-1)
            exit()
        else:
            result = max(result, max(j))

print(result-1)