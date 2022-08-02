import sys

input = lambda: sys.stdin.readline().strip()
N = int(input())
M = int(input())
graph = [list(map(int,input().split())) for _ in range(N)]
plan = list(set((map(lambda x: int(x)-1, input().split()))))

for k in range(N):
    for i in range(N):
        for j in range(N):
            if not graph[i][j] and graph[i][k] and graph[k][j]:
                graph[i][j] = 1


def solution():
    for i in range(1, len(plan)):
        if not graph[plan[i-1]][plan[i]]:
            return "NO"

    return "YES"


print(solution())