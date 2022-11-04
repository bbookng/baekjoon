a = int(input())
b = list(map(int, input()))

result = 0
n = len(b)
cnt = 0

for i in reversed(b):
    tmp = a * i
    print(tmp)
    result += (tmp * (10 ** cnt))
    cnt += 1

print(result)
