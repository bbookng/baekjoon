N, M = map(int,input().split())

def solution(i, arr):
    if i == M:
        print(" ".join(map(str, arr)))
        return

    for j in range(1, N+1):
        solution(i+1, arr+[j])

solution(0, [])

