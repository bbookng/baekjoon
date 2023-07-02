from collections import deque

N, M = map(int, input().split())
board = [list(map(int, input())) for _ in range(N)]

answer = float('inf')

def bfs():
    global answer
    visited = [[0] * M for _ in range(N)]
    visited[0][0] = 1

    q = deque([(0, 0, 1)])
    while q:
        x, y, d = q.popleft()
        if x == N-1 and y == M-1:
            answer = min(answer, d)

        for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                visited[nx][ny] = 1
                if board[nx][ny]:
                    continue
                else:
                    q.append((nx, ny, d+1))



for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            board[i][j] = 0
            bfs()
            board[i][j] = 1

if answer == float('inf'):
    print(-1)
else:
    print(answer)

