C, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

arr.sort(key = lambda x:x[0])
dp = [float('inf')] * (C+1)

for cost, customer in arr:
    for 