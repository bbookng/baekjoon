N, S = map(int, input().split())
arr = list(map(int, input().split()))

left, right = 0, 0
answer = 0
min_ = 100001

while True:
    if answer >= S:
        min_ = min(min_, right-left)
        answer -= arr[left]
        left += 1
    elif right == N:
        break
    else:
        answer += arr[right]
        right += 1

if min_ == 100001:
    print(0)
else:
    print(min_)
