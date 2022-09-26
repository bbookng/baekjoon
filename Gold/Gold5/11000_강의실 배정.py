import heapq, sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

q = []
for s, e in arr:
    q.append([s, e])

q.sort()

room = []
heapq.heappush(room, q[0][1])

for i in range(1, N):
    if q[i][0] < room[0]:
        heapq.heappush(room, q[i][1])
    else:
        heapq.heappop(room)
        heapq.heappush(room, q[i][1])

print(len(room))