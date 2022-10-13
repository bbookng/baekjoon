import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
indegree = [0] * (N+1)
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

def solution():
    result = []
    q = []

    for i in range(1, N+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        # q = deque(sorted(list(q)))
        q.sort()
        now = q.pop(0)
        result.append(now)
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    for i in result:
        print(i, end=' ')

solution()
