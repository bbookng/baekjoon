import sys
input = sys.stdin.readline

S = int(input())
i = 1
total = 0
cnt = 0
while True:
    if total+i > S:
        total -= i
        cnt -= 1
        i += 1
        continue
    total += i
    i += 1
    cnt += 1
    if total == S:
        break

print(cnt)

