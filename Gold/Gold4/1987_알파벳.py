import sys
input = lambda : sys.stdin.readline().strip()

def dfs(x, y, tmp):
    global cnt

    cnt = max(tmp, cnt)

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    check.add(board[x][y])

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < R and 0 <= ny < C:
            if board[nx][ny] not in check:
                dfs(nx, ny, tmp+1)
                check.remove(board[nx][ny])


check = set()
cnt = 0
R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]
dfs(0, 0, 1)
print(cnt)