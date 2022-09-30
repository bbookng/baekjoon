import sys, heapq
input = sys.stdin.readline

def dijkstra(S):
    arr = [float('inf')] * (V + 1)
    q = []
    heapq.heappush(q, (0, S))
    arr[S] = 0
    while q:
        dist, now = heapq.heappop(q)
        if arr[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < arr[i[0]]:
                arr[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    return arr


V, E = map(int, input().split())
graph = [[] for _ in range(V+1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

V1, V2 = map(int, input().split())

distance1 = dijkstra(1)
distance2 = dijkstra(V1)
distance3 = dijkstra(V2)

ans1 = distance1[V1] + distance2[V2] + distance3[V]
ans2 = distance1[V2] + distance3[V1] + distance2[V]

result = min(ans1, ans2)
print("-1" if result == float('inf') else result)
