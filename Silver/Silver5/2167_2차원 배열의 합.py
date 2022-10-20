import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

K = int(input())
for _ in range(K):
    i, j, x, y = map(int, input().split())
    total = 0
    for k in range(i, x+1):
        for l in range(j, y+1):
            total += arr[k-1][l-1]
    print(total)