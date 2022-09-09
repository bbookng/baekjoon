import sys, heapq
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    K = int(input())
    visited = [0] * 1000001
    Q1 = []
    Q2 = []

    for i in range(K):
        a, b = input().split()
        b = int(b)
        if a == 'I':
            heapq.heappush(Q1, (b, i))
            heapq.heappush(Q2, (-b, i))
            visited[i] = 0
        else:
            if b == 1:
                while Q2 and visited[Q2[0][1]] == 1:
                    heapq.heappop(Q2)
                if Q2:
                    visited[Q2[0][1]] = 1
                    heapq.heappop(Q2)
            if b == -1:
                while Q1 and visited[Q1[0][1]] == 1:
                    heapq.heappop(Q1)
                if Q1:
                    visited[Q1[0][1]] = 1
                    heapq.heappop(Q1)

    while Q1 and visited[Q1[0][1]] == 1:
        heapq.heappop(Q1)
    while Q2 and visited[Q2[0][1]] == 1:
        heapq.heappop(Q2)

    if not Q1:
        print('EMPTY')
    else:
        print(-Q2[0][0], Q1[0][0])

