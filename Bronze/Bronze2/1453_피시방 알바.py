N = int(input())
arr = list(map(int, input().split()))

tmp = [0] * 101

result = 0

for i in arr:
    if tmp[i]:
        result += 1
    else:
        tmp[i] = 1


print(result)
