import sys, heapq
input = sys.stdin.readline

N = int(input())
q = []

for _ in range(N):
    num = int(input())
    heapq.heappush(q, num)
    print(q)
    if len(q) % 2:
        for i in range(len(q)//2):
            tmp = heapq.heappop(q)
            if i == len(q)//2:
                print(tmp)
            heapq.heappush(q, tmp)
    else:
        for i in range(len(q) // 2 + 1):
            tmp = heapq.heappop(q)
            if i == len(q)//2 - 1:
                print(tmp)
            heapq.heappush(q, tmp)



