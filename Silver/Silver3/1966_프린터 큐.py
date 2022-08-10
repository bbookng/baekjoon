from collections import deque
import sys
input = lambda : sys.stdin.readline().strip()

T = int(input())

for i in range(T):
    n , m = map(int, input().split())
    arr = deque(list(map(int, input().split())))
    cnt = 0

    while arr:
        max_ = max(arr)
        tmp = arr.popleft()
        m -= 1

        if max_ == tmp:
            cnt += 1
            if m < 0:
                print(cnt)
                break
        else:
            arr.append(tmp)
            if m < 0:
                m = len(arr) - 1