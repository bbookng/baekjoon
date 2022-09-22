import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

size = 2

for i in range(N):
    for j in range(N):
        if board[i][j] == 9:
            board[i][j] = 0
            a, b = i, j

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs():
    visited = [[-1] * N for _ in range(N)]
    q = deque([(a, b)])
    visited[a][b] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == -1 and board[nx][ny] <= size:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))
    return visited


print(bfs())

def find(visited):
    x, y = 0, 0
    tmp = float('inf')
    for i in range(N):
        for j in range(N):
            if visited[i][j] != -1 and 1 <= board[i][j] < size:
                if visited[i][j] < tmp:
                    x, y = i, j
                    tmp = visited[i][j]
    if tmp == float('inf'):
        return None
    else:
        return x, y, tmp

result = 0
ate = 0

while True:
    value = find(bfs())
    print(value)
    if value == None:
        print(result)
        break
    else:
        cx, cy = value[0], value[1]
        result += value[2]
        board[cx][cy] = 0
        ate += 1
        if ate >= size:
            size += 1
            ate = 0







