import sys
input = sys.stdin.readline

N = int(input())
K = int(input())
arr = sorted(list(map(int, input().split())))


def solution():
    if N <= K:
        print(0)
        return

    result = []
    for i in range(1, N):
        result.append(arr[i] - arr[i-1])

    result.sort(reverse=True)
    for _ in range(K-1):
        result.pop(0)

    return sum(result)

print(solution())


