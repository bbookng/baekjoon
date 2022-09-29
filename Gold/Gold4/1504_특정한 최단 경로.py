import sys
input = sys.stdin.readline

N, E = map(int, input().split())
graph = [[float('inf')] * (N+1) for _ in range(N+1)]

for _ in range(E):
    a, b, c = map(int ,input().split())
    graph[a][b] = c
    graph[b][a] = c

for i in range(1, N+1):
    graph[i][i] = 0

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

V1, V2 = map(int, input().split())

if graph[1][V1] == 'inf' or graph[V1][V2] == 'inf' or graph[V2][N] == 'inf':
    ans1 = -1
else:
    ans1 = graph[1][V1] + graph[V1][V2] + graph[V2][N]

if graph[1][V2] == 'inf' or graph[V2][V1] == 'inf' or graph[V1][N] == 'inf':
    ans2 = -1
else:
    ans2 = graph[1][V2] + graph[V2][V1] + graph[V1][N]

print(min(ans1, ans2))
