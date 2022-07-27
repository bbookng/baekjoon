n = int(input())
arr = []
arr2 = []

for i in range(n):
    arr.append(input())

arr = list(set(arr))

for j in arr:
    arr2.append((len(j), j))

arr2.sort()

for idx, word in arr2:
    print(word)