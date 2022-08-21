import sys
input = lambda : sys.stdin.readline().strip()

N = int(input())
cube = [list(map(int, input().split())) for _ in range(N)]

print(cube)