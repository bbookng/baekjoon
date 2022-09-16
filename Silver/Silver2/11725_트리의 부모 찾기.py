import sys
input = lambda :sys.stdin.readline().strip()
sys.setrecursionlimit(10**6)

N = int(input())
graph = [[] for _ in range(N+1)]

def dfs(n):
    for i in graph[n]:
        if par[i] == 0:
            par[i] = n
            dfs(i)

par = [0] * (N + 1)

for _ in range(N-1):
    p, c = map(int, input().split())
    graph[p].append(c)
    graph[c].append(p)

dfs(1)

print(*par[2:], sep='\n')