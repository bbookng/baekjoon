n = int(input())

result = 0

for i in range(1, n+1):
    arr = list(map(int, str(i)))    # i의 각 자릿수를 str을 써서 list로 변환하여 다시 int로 반환
    result = i + sum(arr)           # i와 list의 각 자릿수를 더하여  result값 재정의
    if result == n:                 # result == n 이면
        result = i                  # result를 i로 변경
        print(result)
        break

    if i == n:                      # i == n 이 될 때 까지 생성자가 없다면 0
        print(0)
