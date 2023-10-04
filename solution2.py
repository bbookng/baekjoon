def solution(n, nationality):
    def check(number, array):
        flag = True
        if number in array:
            return False
        for num in array:
            if not check(number, arr[num]):
                flag = False

        return flag


    answer = set()

    arr = [[] for _ in range(n + 1)]

    for a, b in nationality:
        arr[a].append(b)
        arr[b].append(a)

    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            if check(i, arr[j]):
                answer.add((i, j))

    return len(answer)



# 예시 입력
n = 4
nationality = [[1, 2], [2, 3], [1, 3]]

n2 = 5
array = [[1, 2], [2, 3]]

# 함수 호출
result = solution(n, nationality)
print(result)  # 출력 결과: 3
print(solution(n2, array))


