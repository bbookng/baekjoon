import sys
input = sys.stdin.readline

N = int(input())
like = dict()
cls = [[0] * N for _ in range(N)]
check = []


for i in range(N*N):
    num, *students = map(int, input().split())
    like[num] = students
    if i == 0:
        if N % 2:
            cls[N//2][N//2] = num
        else:
            cls[N//2-1][N//2-1] = num
    else:



