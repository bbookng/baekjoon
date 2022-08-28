import sys
input = lambda : sys.stdin.readline().strip()

# def dfs(x, y, tmp):
#     global cnt
#
#     cnt = max(tmp, cnt)
#
#     dx = [1, -1, 0, 0]
#     dy = [0, 0, 1, -1]
#
#     check.add(board[x][y])
#
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#
#         if 0 <= nx < R and 0 <= ny < C:
#             if board[nx][ny] not in check:
#                 dfs(nx, ny, tmp+1)
#                 check.remove(board[nx][ny])

def dfs(i, j, visited):
    global cnt

    if cnt >= 26:
        return

    if cnt < len(visited):
        cnt = len(visited)

    for di, dj in ((0, 1), (1, 0), (-1, 0), (0, -1)):
        ni, nj = i + di, j + dj

        if 0 <= ni < R and 0 <= nj < C:
            if board[ni][nj] not in visited:
                dfs(ni, nj, visited+[board[ni][nj]])

cnt = 0
R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]
dfs(0, 0, [board[0][0]])
print(cnt)