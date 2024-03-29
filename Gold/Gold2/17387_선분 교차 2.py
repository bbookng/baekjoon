import sys

x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
x3, y3, x4, y4 = map(int, sys.stdin.readline().split())


def ccw(x1, y1, x2, y2, x3, y3):
    return (x2 - x1) * (y3 - y2) - (x3 - x2) * (y2 - y1)


res1 = ccw(x1, y1, x2, y2, x3, y3)
res2 = ccw(x1, y1, x2, y2, x4, y4)
res3 = ccw(x3, y3, x4, y4, x1, y1)
res4 = ccw(x3, y3, x4, y4, x2, y2)

if res1 == res2 == res3 == res4 == 0:
    if (max(x1, x2) < min(x3, x4)) or (max(x3, x4) < min(x1, x2)) or (max(y1, y2) < min(y3, y4)) or (max(y3, y4) < min(y1, y2)):
        print(0)
    else:
        print(1)

elif (res1 * res2 <= 0) and (res3 * res4 <= 0):
    print(1)
else:
    print(0)