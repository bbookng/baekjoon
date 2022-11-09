import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
methods = {1: ([0], [1], [2], [3]), 2: ([0, 3], [1, 2]), 3: ([2, 0], [1, 0], [1, 3], [3, 2] ), 4: ([0, 1, 2], [0, 1, 3], [0, 2, 3], [1, 2, 3]), 5: ([0, 1, 2, 3])}
visited = [[0] * M for _ in range(N)]

def solution(i, j):
    tmp = 0
    for case in methods[arr[i][j]]:
        for k in case:
            dx, dy = directions[k]
            x, y = i, j
            while True:
                nx, ny = x + dx, y + dy
                if

for i in range(N):
    for j in range(N):
        if arr[i][j] != 0 and arr[i][j] != 6:
            solution(i, j)



