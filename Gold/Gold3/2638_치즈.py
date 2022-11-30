import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

def solution():
    q = deque()

    q.append((0, 0))
    visited[0][0] = 1

    while q:
        x, y = q.popleft()

        for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            nx, ny = x + dx, y + dy

            if 0 <= nx < N and 0 <=  ny < M:
                if not board[nx][ny] and not visited[nx][ny]:
                    q.append((nx, ny))
                    visited[nx][ny] = 1
                elif board[nx][ny] == 1:
                    visited[nx][ny] += 1

    flag = False

    for i in range(N):
        for j in range(M):
            if visited[i][j] >= 2:
                board[i][j] = 0
                flag = True

    return flag

result = 0

while True:

    visited = [[0] * M for _ in range(N)]
    flag = solution()
    if not flag:
        break
    else:
        result += 1

print(result)


