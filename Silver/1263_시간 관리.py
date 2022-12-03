import sys
input = sys.stdin.readline

N = int(input())

works = [tuple(map(int, input().split())) for _ in range(N)]

works.sort(key=lambda x: x[1])

time = 0
while True:
    total = time

    for t, s in works:
        if total + t <= s:
            total += t
        else:
            print(time-1)
            exit()
    time += 1