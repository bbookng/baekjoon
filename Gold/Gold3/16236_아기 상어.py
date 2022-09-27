import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# 처음 위치 찾기
for i in range(N):
    for j in range(N):
        if arr[i][j] == 9:
            si, sj = i, j
            arr[i][j] = 0
            break
    else:
        continue
    break

size = 2
time = 0
eaten = 0
answer = 0

while True:
    q = deque()
    q.append((time, si, sj))
    visited = [[0] * N for _ in range(N)]
    candidates = []
    limit = 999999
    while q:
        time, ci, cj = q.popleft()
        if limit < time:
            break
        if arr[ci][cj] != 0 and arr[ci][cj] < size:
            candidates.append((ci, cj, time))
            limit = time

        for di, dj in ((-1, 0), (0, -1), (0, 1), (1, 0)):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj] and arr[ni][nj] <= size:
                visited[ni][nj] = 1
                q.append((time+1, ni, nj))
    candidates.sort()
    if candidates:
        si, sj, time = candidates[0]
        answer = time
        arr[si][sj] = 0
        eaten += 1
        if eaten == size:
            size += 1
            eaten = 0
    else:
        break

print(answer)

