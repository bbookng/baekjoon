import sys
input = lambda :sys.stdin.readline().strip()


def dfs(now):
    print(now, end=' ')
    visited[now] = 1
    for i in Graph[now]:
        if not visited[i]:
            dfs(i)
            visited[i] = 1

def BFS(v):
    queue = []
    queue.append(v)
    visited[v] = 1
    while queue:
        v = queue.pop(0)
        print(v, end=' ')
        for w in Graph[v]:
            if not visited[w]:
                queue.append(w)
                visited[w] = visited[v] + 1

N, M, V = map(int, input().split())
Graph = [[] for _ in range(N+1)]
visited = [0] * (N + 1)
for i in range(M):
    a, b = map(int, input().split())
    Graph[a].append(b)
    Graph[b].append(a)

for i in range(len(Graph)):
    Graph[i].sort()

dfs(V)
visited = [0] * (N + 1)
print()
BFS(V)