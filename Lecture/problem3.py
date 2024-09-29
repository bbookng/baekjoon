# 문제 3. 연립방정식 ( # 19532)

A, B, C, D, E, F = map(int, input().split())

for x in range(-10000, 10001):
    for y in range(-10000, 10001):
        if A * x + B * y == C and D * x + E * y == F:
            print(x, y)
            break