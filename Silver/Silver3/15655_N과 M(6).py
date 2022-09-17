N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
chosen = [-1] * M

def solution(n, M, K):
    if n == M:
        print(*chosen)
        return
    else:
        for i in range(K, len(arr)):
            chosen[n] = arr[i]
            solution(n+1, M, i+1)


solution(0, M, 0)








