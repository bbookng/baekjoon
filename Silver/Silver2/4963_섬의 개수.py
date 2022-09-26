import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(i, j):
    arr[i][j] = 0
    for di, dj in ((-1, 0), (1, 0), (0, 1), (0, -1), (-1, -1), (1, 1), (-1, 1), (1, -1)):
        ni, nj = i + di, j + dj
        if 0 <= ni < h and 0 <= nj < w and not arr[ni][nj]:
            dfs(ni, nj)


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    arr = [list(map(int, input().split())) for _ in range(h)]

    cnt = 0

    for i in range(h):
        for j in range(w):
            if arr[i][j] == 1:
                dfs(i, j)
                cnt += 1

    print(arr)

    print(cnt)