import sys, heapq
input = lambda :sys.stdin.readline().strip()

def solution(S):
    Q = []
    heapq.heappush(Q, (0, S))
    visited[S] = 0

    while Q:
        fee, x = heapq.heappop(Q)

        if visited[x] < fee:
            continue

        for nw, nx in graph[x]:
            nd = fee + nw

            if visited[nx] > nd:
                heapq.heappush(Q, (nd, nx))
                visited[nx] = nd

N = int(input())
M = int(input())
arr = [list(map(int, input().split())) for _ in range(M)]
S, E = map(int, input().split())
visited = [float('INF')] * (N+1)

result = []

graph = [[] for _ in range(N + 1)]

for a, b, c in arr:
    graph[a].append((c, b))

solution(S)

print(visited[E])

