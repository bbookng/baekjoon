N, S = map(int, input().split())
numbers = list(map(int, input().split()))

result = 0
for i in range(1<<N):
    subset = []
    for j in range(N):
        if i & (1 << j):
            subset.append(numbers[j])
    if subset and sum(subset) == S:
        result += 1

print(result)

