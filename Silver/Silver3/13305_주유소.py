import sys
input = sys.stdin.readline

N = int(input())
roads = list(map(int, input().split()))
costs = list(map(int, input().split()))

tmp = max(costs)
total = 0

for i in range(N-1):
    if tmp > costs[i]:
        tmp = costs[i]
    total += roads[i] * tmp

print(total)
