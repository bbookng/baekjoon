import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
result = 0

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def solution(r, c, d):
    global result
    q = deque()
    q.append((r, c, 0))
    arr[r][c] = 2
    result += 1
    while q:
        x, y, cnt = q.popleft()
        print(x, y)
        if cnt == 4:
            q.append((x - directions[d][0], y - directions[d][1], 0))
        d = (d-1) % 4
        nx, ny = x + directions[d][0], y + directions[d][1]
        if 0 <= nx < N and 0 <= ny < M and not arr[nx][ny]:
            arr[nx][ny] = 2
            q.append((nx, ny, cnt))
            result += 1
        else:
            d = (d + 1) % 4
            q.append((x, y, cnt+1))

    return result

print(solution(r, c, d))