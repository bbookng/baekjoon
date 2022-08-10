import sys

input = lambda: sys.stdin.readline().strip()

n = int(input())

board = [[0] * 100 for _ in range(100)]

for _ in range(n):
    i, j = map(int,input().split())
    for x in range(i, i+10):
        for y in range(j, j+10):
            board[x][y] = 1

result = 0

for i in range(len(board)):
    result += sum(board[i])

print(result)

