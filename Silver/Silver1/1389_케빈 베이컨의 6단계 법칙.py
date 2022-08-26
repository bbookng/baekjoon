import sys
input = lambda :sys.stdin.readline().strip()

def BFS(S, N):
    visited = [-1] * (N+1)
    queue = []
    queue.append(S)
    visited[S] = 0
    while queue:
        S = queue.pop(0)
        for w in graph[S]:
            if visited[w] == -1:
                queue.append(w)
                visited[w] = visited[S] + 1
    return sum(visited[1:])

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

total = BFS(1, N)
result = 0
for i in range(1, N+1):
    if BFS(i, N) < total:
        total = BFS(i, N)
        result = i

print(result)

