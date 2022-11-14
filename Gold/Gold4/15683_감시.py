import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
methods = {1: ([0], [1], [2], [3]), 2: ([0, 3], [1, 2]), 3: ([2, 0], [1, 0], [1, 3], [3, 2] ), 4: ([0, 1, 2], [0, 1, 3], [0, 2, 3], [1, 2, 3]), 5: ([], [0, 1, 2, 3])}
visited = [[0] * M for _ in range(N)]

def solution(i, j):
    global visited
    max_ = 0
    std = [i[:] for i in visited]
    for case in methods[arr[i][j]]:
        check = [i[:] for i in visited]
        cnt = 0
        for k in case:
            dx, dy = directions[k]
            x, y = i, j
            while True:
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] != 6:
                    if arr[nx][ny] > arr[i][j]:
                        cnt = 0
                        break
                    if not check[nx][ny]:
                        check[nx][ny] = 1
                        cnt += 1
                        x, y = nx, ny
                    else:
                        x, y = nx, ny
                        continue
                else:
                    break

        if cnt > max_:
            max_ = cnt
            std = [i[:] for i in check]

    visited = [i[:] for i in std]



for i in range(N):
    for j in range(M):
        if arr[i][j] == 6:
            visited[i][j] = 1
            continue
        elif arr[i][j] != 0:
            visited[i][j] = 1
            solution(i, j)

result = 0

for i in visited:
    result += i.count(0)

print(result)



