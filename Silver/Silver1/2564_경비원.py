import sys
input = lambda : sys.stdin.readline().strip()

C, R = map(int, input().split())
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
x, y = map(int, input().split())


# W, H = map(int,input().split())
# N = int(input())
# arr = [list(map(int,input().split())) for _ in range(N)]
# s, l = map(int,input().split())
#
# total = 0
# for ms, ml in arr:
#     if ms == s:
#         total += abs(l-ml)
#
#     elif s+ms == 3:
#         total += min(l + ml, 2 * H - l - ml) + H
#
#     elif s+ms == 7:
#         total += min(l + ml, 2 * W - l - ml) + W
#
#     else:
#