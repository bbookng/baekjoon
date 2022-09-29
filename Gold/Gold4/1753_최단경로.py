import sys, heapq
input = sys.stdin.readline
INF = float('INF')

def dijkstra(S):
    q = []
    heapq.heappush(q, (0, S))
    distance[S] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


V, E = map(int, input().split())
K = int(input())
graph = [[] for _ in range(V+1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

distance = [INF] * (V+1)

dijkstra(K)

for i in distance[1:]:
    if i == INF:
        print('INF')
    else:
        print(i)