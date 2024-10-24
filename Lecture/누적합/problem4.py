# 11660
N, M = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]

prefix = [[0] * (N + 1) for _ in range(N + 1)]

for y in range(N):
    for x in range(N):
        prefix[x+1][y+1] = prefix[x][y+1] + prefix[x+1][y] - prefix[x][y] + graph[x][y]

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    print(prefix[x2][y2] - prefix[x2][y1-1] - prefix[x1-1][y2] + prefix[x1-1][y1-1])
