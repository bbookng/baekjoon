import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

def bfs():
    q = deque()
    q.append((home_x, home_y))
    visited = [0 for _ in range(N)]
    while q:
        x, y = q.popleft()
        if abs(x-festival_x) + abs(y-festival_y) <= 1000:
            print('happy')
            return
        for i in range(N):
            if not visited[i]:
                nx, ny = cvs[i]
                if abs(x-nx) + abs(y-ny) <= 1000:
                    visited[i] = 1
                    q.append((nx, ny))
    print('sad')
    return


for _ in range(T):
    N = int(input())
    home_x, home_y = map(int, input().split())
    cvs = [list(map(int, input().split())) for _ in range(N)]
    festival_x, festival_y = map(int, input().split())
    bfs()


