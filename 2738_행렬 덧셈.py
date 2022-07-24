n, m = map(int, input().split())
arr1 = []
arr2 = []

# 두 개의 행렬 입력받기
for _ in range(n):
    arr1.append(list(map(int, input().split())))
for _ in range(n):
    arr2.append(list(map(int, input().split())))

# 행의 숫자만큼 반복하여 각 행렬의 각 열에 있는 idex 끼리 더하기
for i in range(n):
    x, y = arr1[i], arr2[i]
    result = [ x[j] + y[j] for j in range(m) ]
    print(" ".join(map(str, result)))


