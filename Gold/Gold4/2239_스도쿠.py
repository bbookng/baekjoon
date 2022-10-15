import sys
input = sys.stdin.readline

sdoku = [list(map(int, input().split())) for _ in range(9)]

def dfs(idx):
    if idx == 9:
        for i in range(9):
