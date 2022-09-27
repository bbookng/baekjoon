import sys
n = int(sys.stdin.readline())

# dp table reset
d = [[0, []] for _ in range(n+1)]
d[1] = [0, [1]]

for i in range(2, n+1):
    # 1을 빼는 경우
    d[i] = [d[i - 1][0] + 1, d[i-1][1] + [i]]

    # 2로 나누어 떨어지는 경우
    if i % 2 == 0:
        tmp = i if d[i][0] < d[i//2][0] + 1 else i // 2
        d[i] = [min(d[i][0], d[i // 2][0] + 1), d[tmp][1] + [i]]

    # 3으로 나누어 떨어지는 경우
    if i % 3 == 0:
        tmp = i if d[i][0] < d[i // 3][0] + 1 else i // 3
        d[i] = [min(d[i][0], d[i // 3][0] + 1), d[tmp][1] + [i]]

d[n][1] =list(set(d[n][1]))
if len(d[n][1]) > 1:
    d[n][1].sort(reverse=True)
print(d[n][0])
print(*d[n][1])