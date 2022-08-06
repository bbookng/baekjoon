import sys
input= lambda: sys.stdin.readline().strip()


col, row = map(int, input().split())
cut = int(input())

r = [0, row]
c = [0, col]

for i in range(cut):
    x = list(map(int, input().split()))
    if x[0] == 0:
        r.append(x[1])
    else:
        c.append(x[1])

r.sort()
c.sort()


_max = 0
for i in range(1, len(r)):
    for j in range(1, len(c)):
        if (r[i] - r[i-1]) * (c[j] - c[j-1]) > _max:
            _max = (r[i] - r[i-1]) * (c[j] - c[j-1])

print(_max)



