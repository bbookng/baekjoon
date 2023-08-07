min, max = map(int, input().split())
answer = max - min + 1

visited = [0] * answer

# 2부터 max의 제곱수 까지
for i in range(2, int(max**0.5+1)):
    # 제곱수
    square = i ** 2
    for j in range((((min-1)//square)+1) * square, max+1, square):
        if not visited[j-min]:
            visited[j-min] = 1
            answer -= 1

print(answer)
