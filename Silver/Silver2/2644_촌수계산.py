import sys
input = sys.stdin.readline

N = int(input())
a, b = map(int, input().split())
m = int(input())
arr = [list(map(int, input().split())) for i in range(m)]


def dfs(now):
    for nxt in graph[now]:
        if not visited[nxt]:
            visited[nxt] = visited[now]+1
            dfs(nxt)

graph = [[] for _ in range(N+1)]
for i in arr:
    graph[i[0]].append(i[1])
    graph[i[1]].append(i[0])

visited = [0] * (N+1)
dfs(a)
print(visited[b] if visited[b] > 0 else -1)