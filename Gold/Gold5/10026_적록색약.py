import sys
input = lambda: sys.stdin.readline().strip()
sys.setrecursionlimit(10000)

N = int(input())
board = [list(input()) for _ in range(N)]
visitied = [[0] * N for _ in range(N)]

cnt1 = 0
cnt2 = 0

def dfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visitied[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and visitied[nx][ny] == 0:
            if board[x][y] == board[nx][ny]:
                dfs(nx, ny)

for i in range(N):
    for j in range(N):
        if visitied[i][j] == 0:
            dfs(i, j)
            cnt1 += 1

for i in range(N):
    for j in range(N):
        if board[i][j] == 'R':
            board[i][j] = 'G'

visitied = [[0] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if visitied[i][j] == 0:
            dfs(i, j)
            cnt2 += 1

print(cnt1, cnt2)





