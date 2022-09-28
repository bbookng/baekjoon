import sys
input = sys.stdin.readline
from collections import deque

def bfs(x):
    q = deque()
    q.append(x)
    visited[x] = 1
    cnt = 2
    result[x] = 1
    while q:
        tmp = q.popleft()
        for i in graph[tmp]:
            if visited[i] == 0:
                visited[i] = 1
                result[i] = cnt
                cnt += 1
                q.append(i)



N, M, R = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in graph:
    i.sort()

visited = [0] * (N+1)
result = [0] * (N+1)

bfs(R)
print(*result[1:], sep='\n')