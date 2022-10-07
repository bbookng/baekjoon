import sys, heapq
input = sys.stdin.readline

def dijkstra(S):
    q = []
    heapq.heappush(q, (0, S))
    distance[S] = 0
    cities[S].append(S)
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                cities[i[0]] = cities[now] + [i[0]]
                heapq.heappush(q, (cost, i[0]))

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
distance = [float('inf')] * (N+1)
cities = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))

S, E = map(int, input().split())
dijkstra(S)

print(distance[E])
print(len(cities[E]))
print(cities[E])