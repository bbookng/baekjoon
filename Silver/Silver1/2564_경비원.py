import sys
input = lambda : sys.stdin.readline().strip()

C, R = map(int, input().split())
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
x, y = map(int, input().split())

total = 0
for i in arr:
    tmp = 0
    if x < 3:
        if x == i[0]:
            total += abs(i[1] - y)
        elif i[0] < 3:
            if (y-0) + (i[1]-0) < (C-y) + (C - i[1]):
                total += ((y-0) + (i[1]-0) + R)
            else:
                total += ((C-y) + (C - i[1]) + R)
        else:
            if i[0] == 3:
                if x == 1:
                    total += y + i[1]
                elif x == 2:
                    total += y + (R-i[1])
            if i[0] == 4:
                if x == 1:
                    total += (C-y) + i[1]
                elif x == 2:
                    total += (C-y) + (R-i[1])
    else:
        if x == i[0]:
            total += abs(i[1] - y)
        elif i[0] >= 3:
            if (y - 0) + i[1] < (R - y) + (R - i[1]):
                total += (y + i[1] + C)
            else:
                total += ((R - y) + (R - i[1]) + C)
        else:
            if i[0] == 1:
                if x == 3:
                    total += (R - y) + (i[1])
                elif x == 4:
                    total += (R) + (i[1])
            if i[0] == 2:
                if x == 3:
                    total += (R - y) + (C - i[1])
                elif x == 4:
                    total += R + (C - i[1])

print(total)

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