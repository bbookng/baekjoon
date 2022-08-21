import sys
input = lambda : sys.stdin.readline().strip()

W, H = map(int,input().split())
N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
s, l = map(int,input().split())

total = 0
for ms, ml in arr:
    if ms == s:
        total += abs(l-ml)

    elif s+ms == 3:
        total += min(l + ml, 2 * W - l - ml) + H

    elif s+ms == 7:
        total += min(l + ml, 2 * H - l - ml) + W

    elif s+ms == 4:
        total += l + ml

    elif s+ms == 6:
        total += (W-l)+(H-ml) if s == 2 else (W-ml) + (H-l)


    else:
        if s == 1:
            total += (W-l) + ml
        elif s == 2:
            total += l + (H-ml)
        elif s == 3:
            total += (H-l) + ml
        else:
            total += l + (W-ml)

print(total)

