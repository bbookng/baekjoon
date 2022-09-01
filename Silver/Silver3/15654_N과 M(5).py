N, M = map(int,input().split())
numbers = list(map(int, input().split()))
numbers.sort()
chosen = [-1] * M
visited = [0] * N
check = set()

def solution(n, M):
    if n == M:
        print(" ".join(map(str, arr)))
        check.add(tuple(chosen))
        return

    for j in numbers:



solution(0, M)