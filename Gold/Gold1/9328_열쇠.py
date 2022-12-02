import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    h, w = map(int, input().split())
    arr = [list(input()) for _ in range(h)]