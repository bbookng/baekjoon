import sys
input = sys.stdin.readline

T = int(input())




def dfs(now):
    for nxt in graph[now]:
        if not visited[nxt]:
            visited[nxt] = visited[now]+1
            dfs(nxt)

for tc in range(T):
    M, N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(K)]

    graph = [[] for _ in range(max(M, N) + 1)]
    for i in arr:
        graph[i[0]].append(i[1])
    print(graph)
    visited = [0] * K
    print(visited)
    dfs(0)
    print(max(visited))