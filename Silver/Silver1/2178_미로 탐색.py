import sys
from collections import deque
input = lambda :sys.stdin.readline().strip()

def dfs(x, y):
    global cnt

        for i in range(4):
            nx = x + dx[i]
            ny = y + dx[i]

            if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 1:

N, M = map(int, input().split())
board = [list(map(int, input())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(dfs(0, 0))
