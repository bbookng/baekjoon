N, M = map(int,input().split())
numbers = list(map(int, input().split()))
numbers.sort()
chosen = [-1] * M

def solution(n, M):
    if n == M:
        print(" ".join(map(str, arr)))
        return

    for j in numbers:
        if not j in arr:
            solution(i+1, arr + [j])


solution(0, M)