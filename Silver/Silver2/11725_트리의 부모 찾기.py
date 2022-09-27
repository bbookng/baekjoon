# import sys
# input = lambda :sys.stdin.readline().strip()
# sys.setrecursionlimit(10**6)
#
# N = int(input())
# graph = [[] for _ in range(N+1)]
#
# def dfs(n):
#     for i in graph[n]:
#         if par[i] == 0:
#             par[i] = n
#             dfs(i)
#
# par = [0] * (N + 1)
#
# for _ in range(N-1):
#     p, c = map(int, input().split())
#     graph[p].append(c)
#     graph[c].append(p)
#
# dfs(1)
#
# print(*par[2:], sep='\n')

N = int(input())
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

print(graph)

parents = [0] * (N+1)

def solution(now):
    for i in graph[now]:
        if parents[i] == 0:
            parents[i] = now
            solution(i)

solution(1)


print(*parents[2:], sep='\n')
