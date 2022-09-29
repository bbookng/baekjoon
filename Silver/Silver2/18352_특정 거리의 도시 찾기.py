import sys
input = sys.stdin.readline
from collections import deque

def bfs():
    q = deque()
    q.append(X)
    distance[X] = 0
    while q:
        x = q.popleft()
        for i in graph[x]:
            dist = distance[x] + 1
            if distance[i] > dist:
                distance[i] = dist
                q.append(i)

N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)

distance = [float('inf')] * (N+1)
bfs()
result = []
for i in range(1, N+1):
    if distance[i] == K:
        result.append(i)

if result:
    print(*result, sep='\n')
else:
    print(-1)
