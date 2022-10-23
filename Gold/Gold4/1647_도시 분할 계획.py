import sys
input = sys.stdin.readline

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)

    if a == b:
        return
    if rank[a] > rank[b]:
        parent[b] = a
    elif rank[a] < rank[b]:
        parent[a] = b
    else:
        parent[a] = b
        rank[b] += 1

N, M = map(int, input().split())
graph = []
parent = [i for i in range(N+1)]
rank = [0] * (N+1)

for _ in range(M):
    a, b, c = map(int, input().split())
    graph.append((a, b, c))

graph.sort(key=lambda x:x[2])
result = 0
end = 0
for i in graph:

    if find(i[0]) != find(i[1]):
        union(i[0], i[1])
        result += i[2]
        end = i[2]

print(result - end)

