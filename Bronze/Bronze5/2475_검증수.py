a, b, c, d, e = map(int, input().split())
list = [a, b, c, d, e]

total = 0
for i in list:
    total += i * i

result = total % 10

print(result)
