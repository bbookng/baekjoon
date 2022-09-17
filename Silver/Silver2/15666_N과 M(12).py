N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
chosen = [-1] * M
tmp = []

def solution(n, m):
    if n == m:
        if chosen not in tmp:
            tmp.append(chosen)
            print(*chosen)
            return
    else:
        for i in range(len(arr)):
            chosen[n] = arr[i]
            solution(n+1, m)

solution(0, M)