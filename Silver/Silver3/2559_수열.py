import sys
input = lambda : sys.stdin.readline().strip()

N, K = map(int, input().split())
arr = list(map(int, input().split()))

result = []

for i in range(K-1, N):
    tmp = arr[i]
    for j in range(1, K):
        tmp += arr[i-j]
    result.append(tmp)

print(max(result))