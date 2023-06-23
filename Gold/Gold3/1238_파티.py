import heapq

N, M, X = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    s, e, t = map(int, input().split())
    graph[s].append((e, t))

answer = 0

def solution(num):
    visited = [0] * (N+1)

    q = []
    heapq.heappush(q, (0, num))



