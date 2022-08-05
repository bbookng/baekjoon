k, n = map(int, input().split())
arr = [int(input()) for i in range(k)]

start = 1
end = max(arr)

while start <= end:
    num = 0
    mid = (start+end) // 2
    for i in arr:
        num += (i // mid)
    if num < n:
        end = mid-1
    elif num >= n:
        start = mid+1
print(end)
    

