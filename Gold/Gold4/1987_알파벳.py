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

def dfs(i, j, result):
    global cnt

    if result > cnt:
        cnt = result

    for di, dj in ((0, 1), (1, 0), (-1, 0), (0, -1)):
        ni, nj = i + di, j + dj

        if 0 <= ni < R and 0 <= nj < C and check[ord(board[ni][nj]) - 65] == 0:
            check[ord(board[ni][nj]) - 65] = 1
            dfs(ni, nj, result+1)
            check[ord(board[ni][nj]) - 65] = 0


R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]
check = [0] * 26
check[ord(board[0][0]) - 65] = 1
cnt = 0
dfs(0, 0, 1)
print(cnt)