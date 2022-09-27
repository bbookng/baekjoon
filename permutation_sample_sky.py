import sys
sys.setrecursionlimit(10**6)

result = ''

def solution(n, m, x, y, r, c, k):
    global result

    if (k - abs(x-r) + abs(y-c)) % 2:
        return 'impossible'

    if abs(x-r) + abs(y-c) > k:
        return 'impossible'

    def dfs(xi, yi, route, cnt):
        global result

        if cnt == k and xi == r-1 and yi == c-1 and result > route:
            result = route

        for i in {'d': [1, 0], 'l': [0, -1], 'r': [0, 1], 'u': [-1, 0]}:
            nx, ny = xi + i[0], yi + i[1]

            if 0 <= nx < n and 0 <= ny < m and cnt < k:
                dfs(nx, ny, route + i, cnt + 1)

    dfs(x-1, y-1, '', 0)

    return result

print(solution())