import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
methods = {1: (0, 1, 2, 3), 2: (), 3: 3, 4: 4, 5: 1}
visited = [[0] * M for _ in range(N)]

for i in range(N):
    for j in range(N):
        tmp = 0
        if arr[i][j] != 0 and arr[i][j] != 6:
            for k in range(methods[arr[i][j]]):

