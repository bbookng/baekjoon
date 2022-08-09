n, k = map(int, input().split())
arr = list(range(1, n+1))
result = []

idx = 0

while arr:
    idx += k-1
    if idx >= len(arr):
        idx %= len(arr)
    result.append(arr[idx])
    arr.remove(arr[idx])

print('<', end='')
print(", ".join(map(str, result)), end='')
print('>')
