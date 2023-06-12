N = int(input())
graph = [[] for _ in range(N+1)]
route = [[0] * (N+1) for _ in range(N+1)]
print(graph)
print(route)

answer = 0

for _ in range(N-1):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

for i in range(1, N+1):
    for j in range(i+1, N+1):
        print(i, j)