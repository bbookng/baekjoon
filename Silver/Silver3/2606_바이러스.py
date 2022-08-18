import sys
input = lambda : sys.stdin.readline().strip()

def dfs(now):
    visited[now] = 1
    for nxt in graph[now]:
        if not visited[nxt]:
            dfs(nxt)

N = int(input())
L = int(input())
arr = [list(map(int, input().split())) for i in range(L)]

graph = [[] for _ in range(N+1)]
for i in arr:
    graph[i[0]].append(i[1])
    graph[i[1]].append(i[0])

visited = [0] * (N+1)
dfs(1)
print(visited.count(1)-1)