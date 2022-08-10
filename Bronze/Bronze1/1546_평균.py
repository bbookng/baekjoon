n = int(input())
score = list(map(int, input().split()))

result = []

for i in score:
    result.append(i / max(score)*100)

print(sum(result)/n)