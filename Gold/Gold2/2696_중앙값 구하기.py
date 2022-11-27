import sys, heapq
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    M = int(input())
    arr = list(map(int, input().split()))

    heap = []

    for i in range(M):
        heapq.heappush(heap, arr[i])

