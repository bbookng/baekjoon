<<<<<<< HEAD
#
# queries = [[2, 10],[7, 1],[2, 5],[2, 9],[7, 32]]
#
# def solution(queries):
#     answer = 0
#     dic = dict()
#     for arr, nums in queries:
#         if arr in dic:
#             if dic[arr][1] < dic[arr][0] + nums:
#                 while dic[arr][1] >= dic[arr][0] + nums:
#                     dic[arr][1] *= 2
#                 answer += dic[arr][0]
#                 dic[arr][0] += nums
#             else:
#                 dic[arr][0] += nums
#         else:
#             i = 0
#             while True:
#                 if 2**i >= nums:
#                     size = 2**i
#                     break
#                 i += 1
#             dic[arr] = [nums, size]
#     return answer
#
# print(solution(queries))


N, M = 3, 2
fires = [[1, 1]]
ices = [[3, 3]]
ice = [k**2 + (k-1)**2 for k in range(2, M+2)]

def solution(N, M, fires, ices):
    answer = [[]]
    town = [[0]*N for _ in range(N)]
    for k in  range(1, M+1):
        for i in range(k+1):
            for j in range(k+1):
                town[fires[0][0]-1+i][fires[0][1]-1+j] += 1

    dx = [1, -1, 0, 0, -1, -1, 1, 1]
    dy = [0, 0, -1, 1, -1, 1, -1, 1]

    for k in range(1, M+1):
        for i in range(N):
            for j in range(N):
                nx = ices
                if abs(x) + abs(y) <= k and 0 <= x < N and 0 <= y < N:
                    town[x][y] -= 1

    print(town)
    return

solution(N, M, fires, ices)


=======
N, B = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
result = arr[:]

cnt = 0
while cnt != B:
    for i in range(N):
        for j in range(N):
            for k in range(N):
                result[i][j] += result[i][k] * result[k][i]

    cnt += 1
for i in range(N):
    for j in range(N):
        result[i][j] %= 1000
print(result)
>>>>>>> 30ceee7218389cc3a4b6522d86219acc6f00d919
