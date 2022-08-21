import sys
input = lambda : sys.stdin.readline().strip()

N, K = map(int, input().split())
arr = list(map(int, input().split()))


tmp = sum(arr[0:K])
board = [tmp]

for i in range(N-K):
    tmp = tmp - arr[i] + arr[i+K]
    board.append(tmp)

print(max(board))