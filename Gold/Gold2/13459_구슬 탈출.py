import sys
input = lambda :sys.stdin.readline().strip()
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def move(x, y, i, j):
    count = 0
    while arr[x+i][y+j] != '#' and arr[x][y] != 'O':
        x += i
        y += j
        count += 1
    return x, y, count

def bfs():
    q = deque()
    visited = []
    q.append((red_sx, red_sy, blue_sx, blue_sy, 1))
    cnt = 0
    while q:
        red_x, red_y, blue_x, blue_y, cnt = q.popleft()

        if cnt > 10:
            break

        for i in range(4):
            red_nx, red_ny, red_cnt = move(red_x, red_y, dx[i], dy[i])
            blue_nx, blue_ny, blue_cnt = move(blue_x, blue_y, dx[i], dy[i])

            if arr[blue_nx][blue_ny] == 'O':
                continue

            if arr[red_nx][red_ny] == 'O':
                return 1

            if red_nx == blue_nx and red_ny == blue_ny:
                if red_cnt > blue_cnt:
                    red_nx -= dx[i]
                    red_ny -= dy[i]
                else:
                    blue_nx -= dx[i]
                    blue_ny -= dy[i]

            if [red_nx, red_ny, blue_nx, blue_ny] not in visited:
                visited.append([red_nx, red_ny, blue_nx, blue_ny])
                q.append((red_nx, red_ny, blue_nx, blue_ny, cnt + 1))
    return 0

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]

for i in range(N):
    for j in range(M):
        if arr[i][j] == 'R':
            red_sx, red_sy = i, j
        elif arr[i][j] == 'B':
            blue_sx, blue_sy = i, j

print(bfs())