import sys
input = sys.stdin.readline
from collections import deque
INF = 1e9

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

size = 2

for i in range(N):
    for j in range(N):
        if board[i][j] == 9:
            board[i][j] = 0
            x, y = i, j

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]






