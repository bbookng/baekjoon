import sys

N = int(sys.stdin.readline())
matrix = []

# 모든 입력을 한 번에 받아서 처리
data = []
while len(data) < N * N:
    data.extend(map(int, sys.stdin.readline().split()))

# 행렬로 변환
for i in range(N):
    row = data[i * N:(i + 1) * N]
    matrix.append(row)

max_sum = -127 * N * N  # 가능한 최소 합으로 초기화

# 왼쪽 경계부터 오른쪽 경계까지 반복
for left in range(N):
    temp = [0] * N
    for right in range(left, N):
        # 현재 열의 값을 temp에 더하기
        for i in range(N):
            temp[i] += matrix[i][right]

        # 1차원 배열에서의 최대 부분 배열 합 (Kadane's Algorithm)
        current_sum = temp[0]
        current_max = temp[0]
        for i in range(1, N):
            current_sum = max(temp[i], current_sum + temp[i])
            current_max = max(current_max, current_sum)

        # 최대 합 업데이트
        max_sum = max(max_sum, current_max)

print(max_sum)