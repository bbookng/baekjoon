N = int(input())
arr = []

for _ in range(N):
    tmp = list(input().split())
    arr.append(tmp[1:])

arr.sort()

answer = []

for i in range(N):
    if i == 0:
        for j in range(len(arr[i])):
          answer.append('--' * j + arr[i][j])
    else:
        idx = 0
        for j in range(len(arr[i])):
            if arr[i-1][j] != arr[i][j] or len(arr[i-1]) <= j:
                break
            else:
                idx = j + 1
        for j in range(idx, len(arr[i])):
            answer.append('--' * j + arr[i][j])

for i in answer:
    print(i)

