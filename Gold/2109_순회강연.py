import sys, heapq
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

arr.sort(key=lambda x:x[1])
heap = []

for i in arr:
    heapq.heappush(heap, i[0])
    if len(heap) > i[1]:
        heapq.heappop(heap)

print(sum(heap))