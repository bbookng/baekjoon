import sys
input = sys.stdin.readline

N = int(input())
area = 0
x, y = map(int, input().split())
xi, yi = x, y
for _ in range(N-1):
    nx, ny = map(int, input().split())
    area += x * ny - y * nx
    x, y = nx, ny
area += x * yi - y * xi
area = abs(area) / 2

print(round(area,1))
