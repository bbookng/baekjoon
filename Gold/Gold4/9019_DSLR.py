import sys
from collections import deque
input = sys.stdin.readline

def bfs(A):
    q = deque()
    q.append([A, ''])
    while q:
        tmp, method = q.popleft()
        if tmp == B:
            return method
        D = (str(int(tmp)*2 % 10000)).zfill(4)
        S = (str(int(tmp)-1)).zfill(4) if tmp != '0000' else '9999'
        L = tmp[1:] + tmp[0]
        R = tmp[3] + tmp[:3]

        for i in [D, S, L, R]:
            if i == D and not visited[int(D)]:
                q.append([D, method+'D'])
            elif i == S and not visited[int(D)]:
                q.append([S, method + 'S'])
            elif i == L and not visited[int(D)]:
                q.append([L, method + 'L'])
            elif i == R and not visited[int(D)]:
                q.append([R, method + 'R'])


T = int(input())

for _ in range(T):
    A, B = map(lambda x: x.zfill(4), input().split())
    visited = [0] * 10000
    print(bfs(A))


