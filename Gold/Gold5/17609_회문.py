import sys
input = lambda :sys.stdin.readline().strip()
sys.setrecursionlimit(10**6)

# def sol(left, right):
#     while left < right:
#         if s[left] == s[right]:
#             left += 1
#             right -= 1
#         else:
#             return False
#     return True
#
# def sol2(left, right):
#     while left < right:
#         if s[left] == s[right]:
#             left += 1
#             right -= 1
#         else:
#             if sol(left+1, right) or sol(left, right-1):
#                 return 1
#             return 2
#     return 0
#
#
# T = int(input())
# for _ in range(T):
#     s = list(input())
#     print(sol2(0, len(s)-1))

import sys
sys.setrecursionlimit(10**6)

def solution(left, right, flag):
    global ans
    if flag > 1:
        return

    if left >= right:
        ans = flag
        return

    while s[left] == s[right]:
        if right <= left:
            ans = flag
            return
        left += 1
        right -= 1


    else:
        solution(left + 1, right, flag + 1)
        solution(left, right - 1, flag + 1)

T = int(input())

for _ in range(T):
    s = input()
    ans = 2
    solution(0, len(s)-1, 0)
    print(ans)