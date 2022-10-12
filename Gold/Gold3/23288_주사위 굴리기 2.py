import sys
from collections import deque
input = sys.stdin.readline

N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

x, y = 0, 0
d = 1

dice = [1, 2, 3, 4, 5, 6]
dx = [0, 0, 1, 0, -1]
dy = [0, 1, 0, -1, 0]

total = 0

def bfs(i, j):
    cnt = 1
    q = deque()
    q.append((i, j))
    visited = [[0] * M for _ in range(N)]
    visited[i][j] = 1
    while q:
        sx, sy = q.popleft()
        for k in range(1, 5):
            nx, ny = sx + dx[k], sy + dy[k]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                if board[nx][ny] == board[x][y]:
                    cnt += 1
                    q.append((nx, ny))
                    visited[nx][ny] = 1
    return cnt


def update(direction, dice):
    a, b, c, d, e, f = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]
    if direction == 1:
        dice = [d, b, a, f, e, c]
    elif direction == 2:
        dice = [b, f, c, d, a, e]
    elif direction == 3:
        dice = [c, b, f, a, e, d]
    elif direction == 4:
        dice = [e, a, c, d, f, b]
    return dice

for _ in range(K):
    x, y = x + dx[d], y + dy[d]
    if 0 <= x < N and 0 <= y < M:
        dice = update(d, dice)
        total += board[x][y] * bfs(x, y)
        if dice[5] > board[x][y]:
            d = d + 1 if d != 4 else 1
        elif dice[5] < board[x][y]:
            d = d - 1 if d != 1 else 4
    else:
        x, y = x - dx[d], y - dy[d]
        d = d - 2 if d > 2 else d + 2
        x, y = x + dx[d], y + dy[d]
        dice = update(d, dice)
        total += board[x][y] * bfs(x, y)
        if dice[5] > board[x][y]:
            d = d + 1 if d != 4 else 1
        elif dice[5] < board[x][y]:
            d = d - 1 if d != 1 else 4


print(total)


