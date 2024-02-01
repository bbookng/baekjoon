from collections import defaultdict

N, K = map(int, input().split())
numbers = list(map(int, input().split()))

counter = defaultdict(int)

start, end = 0, 0
answer = 0

while end < N:
    if counter[numbers[end]] >= K:
        counter[numbers[start]] -= 1
        start += 1
    else:
        counter[numbers[end]] += 1
        end += 1
        answer = max(answer, end-start)

print(answer)
