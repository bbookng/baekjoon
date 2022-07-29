arr = [int(input()) for _ in range(9)]

for i in arr:
    for j in arr:
        if i != j:
            if sum(arr) - (i+j) == 100:
                arr.remove(i)
                arr.remove(j)
                break


arr = sorted(arr)
print(*arr, sep = '\n')