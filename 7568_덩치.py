import sys

n = int(input())

arr = []

for i in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))


for w1, h1 in arr:
    rank = 1
    for w2, h2 in arr:
        if w1 < w2 and h1 < h2:
            rank += 1
    print(rank, end=" ")





