import sys
input = sys.stdin.readline

N = int(input())
arr = sorted(list(map(int, input().split())))
tmp = 0
total = 0

for i in arr:
    tmp += i
    total += tmp

print(total)