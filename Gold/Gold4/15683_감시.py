import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
methods = {1: ([0], [1], [2], [3]), 2: ([0, 3], [1, 2]), 3: ([2, 0], [1, 0], [1, 3], [3, 2] ), 4: ([0, 1, 2], [0, 1, 3], [0, 2, 3], [1, 2, 3]), 5: ([], [0, 1, 2, 3])}
visited = [[0] * M for _ in range(N)]

sensors = []
for i in range(N):
    for j in range(M):
        if 0 < arr[i][j] < 6:
            sensors.append((i, j, arr[i][j]))

K = len(sensors)

def calculate(i, j, k):
    ks = methods[arr[i][j]][k]
    for k in ks:
        try:
            di, dj = i + directions[k], j + directions[k]

        except:
            continue

_min = float('inf')
def solution(i, total):
    global _min

    if i == K:
        _min = min(total, _min)


    for j in methods[sensors[i][2]]:

        solution(i+1, arr)
