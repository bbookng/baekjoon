import sys
input = sys.stdin.readline

R, C, M = map(int, input().split())
board = [[0] * C for _ in range(R)]

shark = dict()

for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    shark[(r, c)] = (s, d, z)

print(shark)
