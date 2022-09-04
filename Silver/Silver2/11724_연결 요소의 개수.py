import sys
input = sys.stdin.readline
sys.setrecursionlimit(10001)

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
visitied = [0] * (N+1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(now):
    visitied[now] = 1
    for i in graph[now]:
        if visitied[i] == 0:
            dfs(i)

cnt = 0
for i in range(1, N+1):
    if visitied[i] == 0:
        dfs(i)
        cnt += 1

print(cnt)

