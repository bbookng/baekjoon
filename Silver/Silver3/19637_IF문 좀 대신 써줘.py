import sys
input = sys.stdin.readline

N, M = map(int, input().split())
title = [input().split() for _ in range(N)]

def binary_search_power(power):
    left = 0
    right = N - 1

    while left <= right:
        mid = (right + left) // 2
        std = int(title[mid][1])
        if std < power:
            left = mid + 1
        else:
            right = mid - 1

    return left

for _ in range(M):
    power = int(input())
    index = binary_search_power(power)
    print(title[index][0])
