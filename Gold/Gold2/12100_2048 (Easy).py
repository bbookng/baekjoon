import sys
input = sys.stdin.readline
from collections import deque

def move(direction):
    # 상
    if not direction:
        for j in range(N):
            for i in range(N):
                if arr[i][j]:
                    q.append(arr[i][j])

            for i in range(N):
                if len(q) > 1:
                    if q[0] == q[1]:
                        arr[i][j] = q.popleft() * 2
                        q.popleft()
                    else:
                        arr[i][j] = q.popleft()
                elif q:
                    arr[i][j] = q.popleft()
                else:
                    arr[i][j] = 0

    # 하
    if direction == 1:
        for j in range(N):
            for i in range(N-1, -1, -1):
                if arr[i][j]:
                    q.append(arr[i][j])
            for i in range(N):
                if len(q) > 1:
                    if q[0] == q[1]:
                        arr[N-i-1][j] = q.popleft() * 2
                        q.popleft()
                    else:
                        arr[N-i-1][j] = q.popleft()
                elif q:
                    arr[N-i-1][j] = q.popleft()
                else:
                    arr[N-i-1][j] = 0

    # 좌
    if direction == 2:
        for i in range(N):
            for j in range(N):
                if arr[i][j]:
                    q.append(arr[i][j])

            for j in range(N):
                if len(q) > 1:
                    if q[0] == q[1]:
                        arr[i][j] = q.popleft() * 2
                        q.popleft()
                    else:
                        arr[i][j] = q.popleft()
                elif q:
                    arr[i][j] = q.popleft()
                else:
                    arr[i][j] = 0

    # 우
    if direction == 3:
        for i in range(N):
            for j in range(N-1, -1, -1):
                if arr[i][j]:
                    q.append(arr[i][j])

            for j in range(N):
                if len(q) > 1:
                    if q[0] == q[1]:
                        arr[i][N-j-1] = q.popleft() * 2
                        q.popleft()
                    else:
                        arr[i][N-j-1] = q.popleft()
                elif q:
                    arr[i][N-j-1] = q.popleft()
                else:
                    arr[i][N-j-1] = 0


def solve(idx):
    global arr, answer
    if idx == 5:
        for i in range(N):
            answer = max(answer, max(arr[i]))
        return

    b = [x[:] for x in arr]

    for k in range(4):
        move(k)
        solve(idx + 1)
        arr = [x[:] for x in b]

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
q = deque()
answer = 0
solve(0)

print(answer)