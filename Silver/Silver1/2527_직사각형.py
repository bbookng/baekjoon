# import sys
# input = sys.stdin.readline
#
# for _ in range(4):
#     arr = list(map(int, input().split()))
#     sq1 = [arr[i] for i in range(4)]
#     sq2 = [arr[i] for i in range(4, 8)]
#
#     check = set(sq1) & set(sq2)
#
#     if len(check):
#         print('c') if len(check) > 1 else print('b')
#     else:
#         if sq1[0] <= sq2[0] <= sq1[2] or sq1[0] <= sq2[2] <= sq1[2]:
#             print('a')
#         elif sq1[1] <= sq2[1] <= sq1[3] or sq1[1] <= sq2[3] <= sq1[3]:
#             print('a')
#         else:
#             print('d')
#

import sys

input = sys.stdin.readline

for _ in range(4):
    x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())

    if y2 < y3 or y4 < y1 or x2 < x3 or x4 < x1:
        print("d")
    elif (x2 == x3 and y2 == y3) or (x1 == x4 and y1 == y4) or (y1 == y4 and x2 == x3) or (x1 == x4 and y2 == y3):
        print('c')
    elif (y1 == y4 and x1 <= x3 <= x2) or (y1 == y4 and x3 <= x1 <= x4) or (y2 == y3 and x1 <= x3 <= x2) or (
            y2 == y3 and x3 <= x1 <= x4) or (x1 == x4 and y1 <= y3 <= y2) or (x1 == x4 and y3 <= y1 <= y4) or (
            x2 == x3 and y1 <= y3 <= y2) or (x2 == x3 and y3 <= y1 <= y4):
        print('b')
    else:
        print('a')