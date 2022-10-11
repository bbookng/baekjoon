import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
K = int(input())

board = [[0] * (N+2) for _ in range(N+2)]

for _ in range(K):
    a, b = map(int, input().split())
    board[a][b] = 1

L = int(input())
turn = dict()

for _ in range(L):
    X, C = input().split()
    turn[int(X)] = C

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
q = deque()
q.append((1, 1))

x, y = 1, 1
cnt = 0
i = 0

while q:
    cnt += 1

    x, y = x + dx[i], y + dy[i]
    if not 1 <= x <= N or not 1 <= y <= N or (x, y) in q:
        break

    q.append((x, y))

    if board[x][y]:
        board[x][y] = 0
    else:
        q.popleft()

    if cnt in turn:
        if turn[cnt] == 'D':
            i = (i + 1) % 4
        else:
            i = (i - 1) % 4
print(cnt)