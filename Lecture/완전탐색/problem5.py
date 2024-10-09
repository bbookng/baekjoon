# 문제 5. 모이기 (# 1090)

n = int(input())
x = []
y = []
result = [-1] * n

for _ in range(n):
    tx, ty = map(int, input().split())
    x.append(tx)
    y.append(ty)

for i in x:
    for j in y:
        # 체커가 있는 위치에서 다른 좌표로의 거리 계산
        dist = []
        for k in range(n):
            dist.append(abs(x[k] - i) + abs(y[k] - j))

        # 가까운 순으로 정렬하기
        dist.sort()

        # m개의 체커가 같은 곳에 모일 때의 최소 비용을 계산
        tmp = 0
        for m in range(len(dist)):
            d = dist[m]
            tmp += d
            if result[m] == -1:
                result[m] = tmp
            else:
                result[m] = min(tmp, result[m])

print(*result)

# 모든 위치에서

# 모든 친구들의 거리를 계산해서

# 가장 적은 값을 알려주면 되겠죠 !


# 1번 아이디어
# X, Y 를 구분해서 계산해준 뒤에 합쳐서
# 최솟값을 알려주면 됩니다 !


# 2번 아이디어
# 우리가 한 곳에서 모일 때, 비용을 최소화하기 위해서는
# 우리의 집 중 한 곳에서 모이면 된다.

# 3번 아이디어
# 최소 거리를 계산하고 싶다.
# 그리고, 2명이 모여야한다.
# 그 점에서, 가까운 두 명의 거리만 더해주면 되지 않을까 ?

# A번집, B번집, C번집
# [1, 2, 3] / [3, 4, 5], [2, 2, 5]

# 두 사람이 모일 수 있는 최소 거리는 -> 3!


