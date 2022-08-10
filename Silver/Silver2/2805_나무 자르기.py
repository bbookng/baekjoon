import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))


def solution(cut):
    height = 0
    for i in arr:
        height += max((i-cut), 0)

    return height


left = 0
right = 2000000000

answer = 0
while left <= right:
    mid = (left + right) // 2
    if solution(mid) >= m:
        answer = mid
        left = mid + 1

    else:
        right = mid -1

print(answer)



