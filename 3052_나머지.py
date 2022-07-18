num = []

for _ in range(10):
    a = int(input())
    b = a % 42
    num.append(b)

s = set(num)
print(len(s))
