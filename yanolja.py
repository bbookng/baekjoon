# def solution(N):
#     # 문자열 초기화
#     string = "a" * N
#
#     # 문자열을 리스트로 변환하여 처리
#     chars = list(string)
#
#     # 인접한 동일한 문자를 찾아서 변환을 수행
#     i = 0
#     while i < len(chars) - 1:
#         if chars[i] == chars[i + 1]:
#             # 다음 문자로 변환
#             chars[i + 1] = chr(ord(chars[i]) + 1)
#
#             # 변환 이후에 문자열이 "zz"가 되면 변환 종료
#             if chars[i + 1] == "z":
#                 break
#
#             # 이전 문자 삭제
#             del chars[i]
#
#             # 이전 문자가 제거되었으므로 인덱스를 감소시킴
#             i = max(0, i - 1)
#         else:
#             # 다음 문자로 이동
#             i += 1
#
#     # 결과 문자열로 변환하여 반환
#     result = "".join(chars)
#     return result


# def solution(N):
#     stack = []
#
#     for i in range(N):
#         stack.append('a')
#
#         # Perform transformations while there are at least two identical adjacent characters
#         while len(stack) >= 2 and stack[-1] == stack[-2]:
#             stack.pop()
#             stack[-1] = chr(ord(stack[-1]) + 1)
#             if stack[-1] == 'z':
#                 break
#
#     result = ''.join(stack)
#     return result


def solution(N):
    # Edge case: when N is 1, the string is 'a'
    if N == 1:
        return 'a'

    # Initialize an empty result string
    result = ""

    # Calculate the maximum number of transformations that can be performed
    max_transformations = min(N - 1, 25)

    # Append the corresponding transformed characters
    for i in range(max_transformations):
        result += chr(ord('a') + i)

    # Calculate the number of remaining characters ('z')
    remaining_chars = N - 1 - max_transformations

    # Append the remaining 'z' characters
    result += 'z' * remaining_chars

    return result


# 예시 테스트 케이스
print(solution(11))  # 출력: "dba"
print(solution(1))  # 출력: "a"
print(solution(67108876))  # 출력: "zzdc"
