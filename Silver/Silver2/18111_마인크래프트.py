# import sys
# input = sys.stdin.readline
#
# n, m, b = map(int, input().split())
# arr = []
# land = [0] * 256
# for i in range(n):
#     arr.append(list(map(int, input().split())))
#
# for i in arr:
#     for j in i:
#         land[j] += 1



import sys
input = sys.stdin.readline
N, M, B = map(int,input().split())
INF = float('inf')


def solution(x):
    total = 0
    cnt = B
    for i in range(N):
        for j in range(M):
            tmp = arr[i][j] - x
            if tmp >= 0:
                total += 2 * tmp
                cnt += tmp
            else:
                total -= tmp
                cnt += tmp
    if cnt >= 0:
        return total
    else:
        return INF


arr = [list(map(int,input().split())) for _ in range(N)]


answer = INF
for i in range(257):
    x = solution(i)
    if x == INF:
        break
    if answer >= x:
        answer = x
        floor = i

print(answer, floor)
