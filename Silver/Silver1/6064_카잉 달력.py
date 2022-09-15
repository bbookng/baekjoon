import sys
input = sys.stdin.readline

def solution(M, N, x, y):
    while x <= N*M:
        if (x-y) % N == 0:
            return x
        x += M
    return -1


T = int(input())

for tc in range(T):
    M, N, x, y = map(int, input().split())

    print(solution(M, N, x, y))

