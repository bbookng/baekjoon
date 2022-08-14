import sys
input = sys.stdin.readline

C, R = map(int,input().split())
N = int(input())
cnt = 0

if N > C*R:
    print(0)
else:
    while N > 2 * (C + R - 2):
        cnt += 1
        N -= 2 * (C + R - 2)
        C -= 2
        R -= 2

    if N < R:
        print(1 + cnt, N + cnt)
    elif N < R+C:
        print(1 + cnt - R + N, cnt + R)
    elif N < 2 * R + C - 1:
        print(cnt + C, cnt + R - 1 - (N-R-C))
    else:
        print(cnt + C - 2 - (N - 2*R - C), cnt + 1)
