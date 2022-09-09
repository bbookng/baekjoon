import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [i for i in range(101)]
visited = [0] * 101

for _ in range(N+M):
    x, y = map(int, input().split())
    graph[x] = y


def bfs():
    q = deque([1])
    while q:
        now = q.popleft()
        for i in range(1, 7):
            next = now + i
            if next <= 100:
                tmp = graph[next]
                if visited[tmp] == 0:
                    q.append(tmp)
                    visited[tmp] = visited[now] + 1
                    if tmp == 100:
                        return visited[100]



print(bfs())