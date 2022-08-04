n = int(input())

arr = []
for _ in range(n):
    arr.append(int(input()))

stack = []
result = []
idx = 0
for i in range(1, n+1):
    stack.append(i)
    result.append('+')

    while stack:
        if stack[-1] == arr[idx]:
            stack.pop()
            result.append('-')
            idx += 1
        else:
            break

if n == idx:
    for j in result:
        print(j)
else:
    print('NO')