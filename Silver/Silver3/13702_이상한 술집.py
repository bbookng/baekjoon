n, k = map(int, input().split())
makgeolli = [int(input()) for _ in range(n)]

start = 1
end = max(makgeolli)

answer = 0
while start <= end:
    mid = (start + end) // 2
    count = sum(i // mid for i in makgeolli)
    if count >= k:
        answer = mid
        start = mid + 1
    else:
        end = mid - 1

print(answer)