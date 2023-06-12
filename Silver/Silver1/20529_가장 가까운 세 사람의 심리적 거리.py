T = int(input())
def solution():
    N = int(input())
    mbti = list(input().split(' '))
    answer = float('inf')
    if N > 32:
        print(0)
    else:
        for i in range(N):
            for j in range(N):
                for k in range(N):
                    score = 0
                    if i == j or j == k or i == k:
                        continue
                    for l in range(4):
                        if mbti[i][l] != mbti[j][l]:
                            score += 1
                        if mbti[j][l] != mbti[k][l]:
                            score += 1
                        if mbti[i][l] != mbti[k][l]:
                            score += 1
                    answer = min(score, answer)
        print(answer)

for _ in range(T):
    solution()

