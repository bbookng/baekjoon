# 2559
N, K = map(int, input().split())
arr = list(map(int, input().split()))

results = [0] * N
results[0] = arr[0]

answer = sum(arr[:K])

for i in range(1, N):
    results[i] = results[i-1] + arr[i]

for i in range(K, N):
    if results[i] - results[i-K] > answer:
        answer = results[i] - results[i-K]

print(answer)
