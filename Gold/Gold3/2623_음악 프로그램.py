import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
indegree = [0] * (N+1)
graph = [[] for _ in range(N+1)]

for _ in range(M):
    arr = list(map(int, input().split()))
    for i in range(1, len(arr) - 1):
        graph[arr[i]].append(arr[i+1])
        indegree[arr[i+1]] += 1

def solution():
    result = []
    q = deque()

    for i in range(1, N+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)

        for i in graph[now]:
            indegree[i] -= 1

            if indegree[i] == 0:
                q.append(i)

    if len(result) != N:
        print(0)
    else:
        print(*result, sep='\n')

solution()
