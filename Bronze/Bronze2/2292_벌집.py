n = int(input())

cnt = 1
count = 1

while n > cnt:
    cnt += 6 * count
    count += 1

print(count)