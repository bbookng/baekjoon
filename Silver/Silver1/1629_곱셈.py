import sys
input = sys.stdin.readline

def sol(A, B, C):
    if B == 1:
        return A % C
    else:
        tmp = sol(A, B//2, C)

    if B % 2 == 0:
        return tmp ** 2 % C
    else:
        return tmp ** 2 * A % C

A, B, C = map(int, input().split())

print(sol(A, B, C))
