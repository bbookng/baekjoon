n = int(input())

# for i in range(1, n+1):
#     print((i * '*').rjust(n, ' '))    # 오른쪽 정렬함수 사용

for i in range(1, n+1):
    print(((n-i)*' ')+(i*'*'))  # 문자열을 더하는 방법 사용