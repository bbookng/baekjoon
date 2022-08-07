# answer = [[''] * 8 for _ in range(8)]
# for i in range(8):
#     for j in range(8):
#         if (i+j)%2:
#             answer[i][j] = 'B'
#         elif not (i+j)%2:
#             answer[i][j] = 'W'
# print(answer)

import sys
input = sys.stdin.readline

N, M = map(int,input().split())
arr = [input() for _ in range(N)]

def solution(i, j):
    cnt = 0
    for a in range(8):
        for b in range(8):
            if (a+b) % 2 and arr[i+a][j+b] == "B":
                cnt += 1
            elif not (a+b) % 2 and arr[i+a][j+b] == "W":
                cnt += 1
    return min(cnt, 64-cnt)


ans = 32
for i in range(N-7):
    for j in range(M-7):
        ans = min(ans, solution(i, j))

print(ans)
