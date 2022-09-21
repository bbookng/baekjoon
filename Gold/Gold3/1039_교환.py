def solution(idx, cnt):
    global result

    if numbers[0] == 0:
        result = -1
        return

    if cnt == N:
        if flag and numbers.count(max(numbers, key=lambda x: numbers.count(x))) == 1:
            numbers[-2], numbers[-1] = numbers[-1], numbers[-2]
        result = max(int(''.join(numbers)), result)
        return
    for i in range(idx, len(numbers)):
        for j in range(idx+1, len(numbers)):
            if numbers[i] < numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]
                solution(idx, cnt + 1)
                numbers[i], numbers[j] = numbers[j], numbers[i]

    if result == 0 and cnt < N:
        if not flag and numbers.count(max(numbers, key=lambda x: numbers.count(x))) == 1:
            numbers[-1], numbers[-2] = numbers[-2], numbers[-1]
        solution(idx, cnt+1)

numbers, N = input().split()
numbers = list(numbers)
N = int(N)

flag = 0

if N > len(numbers):
    flag = (N-len(numbers)) % 2
    N = len(numbers)
result = -1

solution(0, 0)
print(result)