import sys
input = lambda : sys.stdin.readline().strip()

N, K = map(int, input().split())
arr = list(map(int, input().split()))


tmp = sum(arr[0:K])
board = [tmp]
start = 0
end = K

for _ in range(N-K):
    tmp -= arr[start]
    tmp += arr[end]
    start += 1
    end += 1
    board.append(tmp)

print(max(board))