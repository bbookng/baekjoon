N = int(input())

_max = 0

for i in range(1, N+1):
    arr = [N, i]
    while True:
        if arr[-2] - arr[-1] < 0:
            break
        arr.append(arr[-2]-arr[-1])

    if _max < len(arr):
        _max = len(arr)
        result = arr

print(_max)
print(*result)



