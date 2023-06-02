N = int(input())
numbers = sorted(list(map(int, input().split())))
answer = 0

nums = []

for i in range(N):
    for j in range(N):
        if i != j and numbers[i] + numbers[j] in numbers:
            nums.append(numbers[i] + numbers[j])

nums = sorted(nums)

for num in nums:
    left = 0
    right = len(numbers) - 1

    while left != right:
        tmp = numbers[left] + numbers[right]
        if tmp == num:
            answer += 1
            print(numbers[left], numbers[right], tmp, num)
            break
        elif tmp < num:
            left += 1
        elif tmp > num:
            right -= 1

print(answer)



