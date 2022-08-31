import sys
input = lambda: sys.stdin.readline().strip()

def bfs1(x, y):
    visited = [[0] * N for _ in range(N)]
    q = []
    q.append(x, y)
    while q:




N = int(input())
board = [list(input()) for _ in range(N)]

for i in range(N):
    for j in range(N):
