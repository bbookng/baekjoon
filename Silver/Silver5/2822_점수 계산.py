arr = []
for i in range(8):
    arr.append((i+1, int(input())))

arr.sort(key=lambda x:x[1], reverse=True)
total = 0
for i in range(5):
    total += arr[i][1]
print(total)

result = []
for i in range(5):
    result.append(arr[i][0])

result.sort()
print(*result)
