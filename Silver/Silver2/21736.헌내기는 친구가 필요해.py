from collections import deque

N, M = map(int, input().split())
campus = [list(input()) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
answer = 0

def solution(r, c):
    global answer
    q = deque([(r, c)])

    while q:
        x, y = q.popleft()
        visited[x][y] = 1

        for dx, dy in ((-1, 0), (1, 0), (0, 1), (0, -1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                if campus[nx][ny] == 'X':
                    visited[nx][ny] = 1
                else:
                    if campus[nx][ny] == 'P':
                        answer += 1
                    visited[nx][ny] = 1
                    q.append((nx, ny))

    print(answer) if answer else print('TT')

for i in range(N):
    for j in range(M):
        if campus[i][j] == 'I':
            solution(i, j)
            break