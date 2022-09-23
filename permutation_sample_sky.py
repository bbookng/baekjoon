N, B = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
result = arr[:]

cnt = 0
while cnt != B:
    for i in range(N):
        for j in range(N):
            for k in range(N):
                result[i][j] += result[i][k] * result[k][i]

    cnt += 1
for i in range(N):
    for j in range(N):
        result[i][j] %= 1000
print(result)