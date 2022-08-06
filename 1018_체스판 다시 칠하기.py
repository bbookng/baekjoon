import sys
input = sys.stdin.readline

n, m = map(int, input().split())

board = []

for i in range(n):
    board.append(input())

print(board)