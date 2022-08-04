k = int(input())

arr = []
for i in range(k):
    arr.append(int(input()))

result = []
for j in arr:
    if j != 0:
        result.append(j)
    elif j == 0:
        result.pop()

print(sum(result))
