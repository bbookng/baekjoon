# today = "2022.05.19"
#
# terms = ["A 6", "B 12", "C 3"]
# privacies = ["2021.05.02 A", "2021.07.01 B"]
#
#
# def solution(today, terms, privacies):
#     answer = []
#     terms = [term.split() for term in terms]
#     dic = dict()
#     today = list(map(int, today.split('.')))
#
#     for term in terms:
#         dic[term[0]] = int(term[1])
#
#     for i in range(len(privacies)):
#         tmp = privacies[i].split()
#         privacy = list(map(int, tmp[0].split('.')))
#         privacy[1] += dic[tmp[1]]
#
#
#         while privacy[1] > 12:
#             privacy[0] += 1
#             privacy[1] -= 12
#             print(privacy)
#
#         if privacy[0] < today[0]:
#             answer.append(i+1)
#         elif privacy[0] == today[0] and privacy[1] < today[1]:
#             answer.append(i+1)
#         elif privacy[0] == today[0] and privacy[1] == today[1] and privacy[2] <= today[2]:
#             answer.append(i+1)
#
#     return answer
#
# print(solution(today, terms, privacies))

# cap = 4
# n = 5
# deliveries = [1, 0, 3, 1, 2]
# pirckups = [0, 3, 0, 4, 0]
#
#
# def solution(cap, n, deliveries, pickups):
#     answer = float('inf')
#     i = n-1
#     j = n-1
#     weight = 4
#     while i != 0:
#         if deliveries[i] >= cap:
#             deliveries[i] -= cap
#             weight -= cap
#         if pickups[i]:
#
#         if weight == cap:
#             answer += i
#             weight = 0
#
#
#
#     return answer


# users = [[40, 10000], [25, 10000]]
# emoticons = [7000, 9000]
#
# def solution(users, emoticons):
#     answer = []
#     discount = 40
#     limit = 40
#
#     plus = 0
#     sales = 0
#
#     for i in users:
#         limit = min(limit, i[0])
#
#     while discount > limit:
#         for user in users:
#             for emoticon in emoticons:
#
#     return answer

# from collections import deque
# n, m, x, y, r, c, k = 3, 4, 2, 3, 3, 1, 5
#
# def solution(n, m, x, y, r, c, k):
#     direction = {'l': [0, -1], 'r': [0, 1], 'u': [-1, 0], 'd': [1, 0]}
#
#     q = deque([])
#     q.append((x, y, '', 0))
#
#     result = []
#
#     while q:
#         x, y, route, count = q.popleft()
#
#         if count == k:
#             if x == r and y == c:
#                 result.append(route)
#
#         for i in direction:
#             nx, ny = x + direction[i][0], y + direction[i][1]
#             if 0 < nx <= n and 0 < ny <= m and count < k:
#                 q.append((nx, ny, route + i, count + 1))
#
#     result.sort()
#
#     if result:
#         return result[0]
#     else:
#         return 'impossible'
#
#
# solution(n, m, x, y, r, c, k)

cnt = 1


def solution(numbers):
    global cnt
    answer = []

    def inorder(n):
        global cnt
        if n <= j:
            inorder(2 * n)
            if cnt <= j:
                tree[n] = cnt
            else:
                tree[n] = 0
            cnt += 1
            inorder(2 * n + 1)

    for i in numbers:
        check = []
        tmp = 1
        full = 0
        while full < i:
            full = (2 ** tmp) - 1
            tmp += 1

        for j in [full, i]:
            tree = [0] * (full + 1)
            cnt = 1
            inorder(1)
            print(tree)
            print(tree.index(j), tree.index(j//2))

        # if check[0] == check[1]:
        #     answer.append(1)
        # else:
        #     answer.append(0)

    return answer

print(solution([7, 5]))
print(solution([63, 111, 95]))

#
# result = ''
# def solution(n, m, x, y, r, c, k):
#     global result
#     direction = {'d': [1, 0], 'l': [0, -1], 'r': [0, 1], 'u': [-1, 0]}
#     result = 'z'
#
#     if (k - abs(x-r) + abs(y-c)) % 2:
#         return 'impossible'
#
#     if abs(x-r) + abs(y-c) > k:
#         return 'impossible'
#
#     def dfs(xi, yi, route, cnt):
#         global result
#
#         if cnt == k and xi == r-1 and yi == c-1 and result > route:
#             result = route
#
#         for i in direction:
#             nx, ny = xi + direction[i][0], yi + direction[i][1]
#
#             if 0 <= nx < n and 0 <= ny < m and cnt < k:
#                 dfs(nx, ny, route + i, cnt + 1)
#
#     dfs(x-1, y-1, '', 0)
#
#     return result
#
# print(solution(3, 4, 2, 3, 3, 1, 5))
#
#
# cnt = 1
#
# def solution(numbers):
#     global cnt
#     answer = []
#
#     def inorder(n):
#         global cnt
#         if n <= i:
#             inorder(2 * n)
#             tree[n] = cnt
#             cnt += 1
#             inorder(2 * n + 1)
#
#     for i in numbers:
#         tree = [0] * (i + 1)
#         inorder(1)
#         cnt = 1
#         print(tree)
#         if i % 2:
#             answer.append(1) if tree[i//2] < i else answer.append(0)
#         else:
#             answer.append(1) if tree[i//2] > i else answer.append(0)
#
#     return answer
#
# print(solution([7, 5]))
# print(solution([63, 111, 95]))
#
#
#


import sys

sys.setrecursionlimit(10 ** 6)

result = ''


def solution(n, m, x, y, r, c, k):
    global result

    result = 'z'

    if abs(x - r) + abs(y - c) > k:
        return 'impossible'

    if (k - abs(x - r) + abs(y - c)) % 2:
        return 'impossible'

    def dfs(xi, yi, route, cnt):
        global result
        if result < route:
            return

        if cnt == k and xi == r - 1 and yi == c - 1 and result > route:
            result = route

        for a, dx, dy in (('d', 1, 0), ('l', 0, -1), ('r', 0, 1), ('u', -1, 0)):
            nx, ny = xi + dx, yi + dy

            if 0 <= nx < n and 0 <= ny < m and cnt < k:
                dfs(nx, ny, route + a, cnt + 1)

    dfs(x - 1, y - 1, '', 0)

    return result