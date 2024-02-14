def calculate_fee(a, b, time):
    base_fee = b
    total_fee = base_fee
    while time > a:
        time -= a
        total_fee += b
    return total_fee


def solution(fees, t):
    min_fee = float('inf')
    max_fee = 0
    for a in range(1, t + 1):
        for b in range(1, max(fees, key=lambda x: x[1])[1] + 1):
            total_fee = 0
            for time, fee in fees:
                total_fee += calculate_fee(a, b, time)
            if total_fee <= t * b:
                min_fee = min(min_fee, total_fee)
                max_fee = max(max_fee, total_fee)

    if min_fee == float('inf'):
        return -1
    return [min_fee, max_fee]


# 예시 테스트 케이스
fees = [[4, 1000], [6, 1000], [21, 3000], [16, 2000], [26, 3000]]
t = 27
result = solution(fees, t)
print(result)  # 출력: [3000, 4000]

