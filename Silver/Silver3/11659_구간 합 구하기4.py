import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
tmp = [0]
total = 0

for i in arr:
    total += i
    tmp.append(total)

for _ in range(M):
    s, e = map(int, input().split())
    print(tmp[e]-tmp[s-1])

