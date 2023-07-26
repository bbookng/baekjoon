N = int(input())
scovilles = sorted(list(map(int, input().split())))

std = 1000000007
answer = 0

for i in range(N):
    answer += scovilles[i]*(pow(2, i, std)-pow(2, N-i-1, std))

print(answer % std)
