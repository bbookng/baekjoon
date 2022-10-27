import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline

def bfs(tmp, nx, ny):
    q = deque()
    total = 0
    q.append((nx, ny))
    while q:
        si, sj = q.popleft()
        for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            ni, nj = si + di, sj + dj
            if 0 <= ni < N and 0 <= nj < M and not tmp[ni][nj]:
                tmp[ni][nj] = 2
                q.append((ni, nj))

    for i in arr:
        total += i.count(0)
    return total
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
result = 0

comList = []
for i in range(N):
    for j in range(M):
        if not arr[i][j]:
            comList.append((i, j))

for com in combinations(comList, 3):
    tmp = [line[:] for line in arr]
    total = 0

    for x, y in com:
        tmp[x][y] = 1

    for i in range(N):
        for j in range(M):
            if tmp[i][j] == 2:
                bfs(i, j)

    for i in tmp:
        total += i.count(0)

    result = max(result, total)





