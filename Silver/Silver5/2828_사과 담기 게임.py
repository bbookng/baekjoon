N, M = map(int, input().split())
J = int(input())

apple = []
result = 0

for _ in range(J):
    apple.append(int(input()))

end = M
start = 1

for i in range(J):
    if end >= apple[i] and start <= apple[i]:
        continue
    elif end < apple[i]:
        result += apple[i] - end
        end = apple[i]
        start = apple[i] - (M - 1)
    elif start > apple[i]:
        result += start - apple[i]
        start = apple[i]
        end = apple[i] + (M - 1)

print(result)


