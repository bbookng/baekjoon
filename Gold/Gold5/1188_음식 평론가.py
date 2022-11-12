import sys
input = sys.stdin.readline

N, M = map(int, input().split())

def solution(a, b):
    if a % b == 0:
        return b
    return solution(b, a % b)

print(M - solution(N, M))