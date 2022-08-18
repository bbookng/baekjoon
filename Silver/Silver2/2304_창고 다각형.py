import sys
import xml.sax.handler

input = lambda : sys.stdin.readline().strip()

N = int(input())
storage = dict()
for _ in range(N):
    L, H = map(int, input().split())
    storage[L] = H

storage = sorted(storage.items())
x = []
y = []
for i in storage:
    x.append(i[0])
    y.append(i[1])

total = 0
tmp_x = 0
tmp_y = 0
for i in range(N):
    if y[i] > tmp_y:
        total += (x[i] - tmp_x) * y[i]
        tmp_y = y[i]
        tmp_x = x[i]
    else:
        if y[i] == max(y):
            if y[i+1] != max(y):
                total += (x[i]-tmp_x) * tmp_y
                tmp_x = x[i]
                tmp_y = y[i]
        if i == N-1:
            total += (x[i]-tmp_x)*(y[i]*tmp_y)

print(total)



