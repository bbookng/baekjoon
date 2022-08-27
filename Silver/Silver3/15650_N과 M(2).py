import sys
input = sys.stdin.readline

N, M = map(int, input().split())

def solution(i):
    if len(tmp) == M:
        print(" ".join(map(str, tmp)))
        return

    for j in range(i, N+1):
        if j not in tmp:
            tmp.append(j)
            solution(j+1)
            tmp.pop()

tmp = []
solution(1)

